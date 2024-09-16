import mysql.connector
from datetime import date, time

# Create a connection to the MySQL database
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="username",
        password="password",
        database="database"
    )

# Section Class
class Section:
    def __init__(self, section_id, section_name, max_capacity=6):
        self.section_id = section_id  # Unique identifier for the section
        self.section_name = section_name  # Name of the section
        self.max_capacity = max_capacity  # Maximum capacity of the section (default is 6)
    
    @staticmethod
    def generate_section_id(cursor):
        cursor.execute("SELECT COUNT(*) FROM Sections;")  # Count existing sections
        count = cursor.fetchone()[0]
        new_id = f"SEC-{count + 1:03d}"  # Generate new section ID
        return new_id
    
    def save(self, cursor):
        section_id = self.generate_section_id(cursor)  # Generate ID for new section
        query = '''
            INSERT INTO Sections (section_id, section_name, max_capacity)
            VALUES (%s, %s, %s)
        '''
        cursor.execute(query, (section_id, self.section_name, self.max_capacity))  # Insert section into database
        print(f"Section created with ID: {section_id}")

# Member Class
class Member:
    def __init__(self, first_name, last_name, email, mobile_phone, age):
        self.first_name = first_name  # Member's first name
        self.last_name = last_name  # Member's last name
        self.email = email  # Member's email address
        self.mobile_phone = mobile_phone  # Member's mobile phone number
        self.age = age  # Member's age
    
    @staticmethod
    def generate_member_id(cursor):
        cursor.execute("SELECT COUNT(*) FROM Members;")  # Count existing members
        count = cursor.fetchone()[0]
        new_id = f"MEM-{count + 1:03d}"  # Generate new member ID
        return new_id
    
    def save(self, cursor):
        member_id = self.generate_member_id(cursor)  # Generate ID for new member
        query = '''
            INSERT INTO Members (member_id, first_name, last_name, email, mobile_phone, age)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(query, (member_id, self.first_name, self.last_name, self.email, self.mobile_phone, self.age))  # Insert member into database
        print(f"Member created with ID: {member_id}")

    @staticmethod
    def delete(cursor, member_id):
        cursor.execute('DELETE FROM Reservations WHERE member_id = %s', (member_id,))  # Remove member's reservations
        cursor.execute('DELETE FROM SubscriptionPacks WHERE member_id = %s', (member_id,))  # Remove member's subscription packs
        cursor.execute('DELETE FROM Members WHERE member_id = %s', (member_id,))  # Remove member from database
        print(f"Member {member_id} and all related data deleted.")

# Subscription Pack Class
class SubscriptionPack:
    def __init__(self, member_id, section_id, pack_type):
        self.member_id = member_id  # ID of the member
        self.section_id = section_id  # ID of the section
        self.pack_type = pack_type  # Type of subscription pack ('8-visit' or '15-visit')
        self.visits_per_month = 8 if pack_type == '8-visit' else 15  # Set number of visits based on pack type
        self.remaining_visits = self.visits_per_month  # Initialize remaining visits to total visits
    
    @staticmethod
    def generate_subscription_id(cursor):
        cursor.execute("SELECT COUNT(*) FROM SubscriptionPacks;")  # Count existing subscriptions
        count = cursor.fetchone()[0]
        new_id = f"SUB-{count + 1:03d}"  # Generate new subscription ID
        return new_id
    
    def save(self, cursor):
        subscription_id = self.generate_subscription_id(cursor)  # Generate ID for new subscription
        query = '''
            INSERT INTO SubscriptionPacks (subscription_id, member_id, section_id, visits_per_month, remaining_visits)
            VALUES (%s, %s, %s, %s, %s)
        '''
        cursor.execute(query, (subscription_id, self.member_id, self.section_id, self.visits_per_month, self.remaining_visits))  # Insert subscription into database
        print(f"Subscription created with ID: {subscription_id}, visits: {self.visits_per_month}")

    def update_remaining_visits(self, cursor, new_remaining_visits):
        query = '''
            UPDATE SubscriptionPacks
            SET remaining_visits = %s
            WHERE member_id = %s AND section_id = %s
        '''
        cursor.execute(query, (new_remaining_visits, self.member_id, self.section_id))  # Update remaining visits in database

    def check_remaining_visits(self, cursor):
        query = '''
            SELECT remaining_visits FROM SubscriptionPacks
            WHERE member_id = %s AND section_id = %s
        '''
        cursor.execute(query, (self.member_id, self.section_id))
        result = cursor.fetchone()
        if result:
            return result[0]  # Return remaining visits
        else:
            print("Subscription not found.")
            return 0  # Return 0 if subscription not found

# Reservation Class
class Reservation:
    def __init__(self, member_id, section_id, reservation_date, reservation_time):
        self.member_id = member_id  # ID of the member
        self.section_id = section_id  # ID of the section
        self.reservation_date = reservation_date  # Date of the reservation
        self.reservation_time = reservation_time  # Time of the reservation

    @staticmethod
    def generate_reservation_id(cursor):
        cursor.execute("SELECT COUNT(*) FROM Reservations;")  # Count existing reservations
        count = cursor.fetchone()[0]
        new_id = f"RES-{count + 1:03d}"  # Generate new reservation ID
        return new_id

    def save(self, cursor, subscription_pack):
        remaining_visits = subscription_pack.check_remaining_visits(cursor)  # Check remaining visits
        if remaining_visits <= 0:
            print(f"Member {self.member_id} has no remaining visits for this section.")
            return

        query = '''
            SELECT COUNT(*) FROM Reservations
            WHERE section_id = %s AND reservation_date = %s AND reservation_time = %s
        '''
        cursor.execute(query, (self.section_id, self.reservation_date, self.reservation_time))
        count = cursor.fetchone()[0]
        if count >= 6:
            print(f"Time slot full for section {self.section_id} on {self.reservation_date} at {self.reservation_time}.")
            return

        reservation_id = self.generate_reservation_id(cursor)  # Generate ID for new reservation
        query = '''
            INSERT INTO Reservations (reservation_id, member_id, section_id, reservation_date, reservation_time)
            VALUES (%s, %s, %s, %s, %s)
        '''
        cursor.execute(query, (reservation_id, self.member_id, self.section_id, self.reservation_date, self.reservation_time))  # Insert reservation into database
        subscription_pack.update_remaining_visits(cursor, remaining_visits - 1)  # Update remaining visits
        print(f"Reservation created with ID: {reservation_id}, remaining visits: {remaining_visits - 1}")

# Function to display menu
def display_menu():
    print("\n===== Member Management System =====")
    print("1. Create Section")
    print("2. Add Member")
    print("3. Subscribe Member to Section")
    print("4. Make a Reservation")
    print("5. Delete Member")
    print("6. Display Sections")
    print("7. Display Members")
    print("8. Display Subscription Packs")
    print("9. Display Reservations")
    print("10. Exit")
    choice = input("Enter your choice: ")
    return choice

# Function to display reservations
def display_reservations(cursor):
    cursor.execute("SELECT * FROM Reservations;")  # Fetch all reservations
    reservations = cursor.fetchall()
    for reservation in reservations:
        reservation_id, member_id, section_id, reservation_date, reservation_time = reservation
                
        # Format `reservation_date` and `reservation_time` for display
        try:
            formatted_date = reservation_date.strftime('%Y-%m-%d') if isinstance(reservation_date, date) else str(reservation_date)
            formatted_time = reservation_time.strftime('%H:%M:%S') if isinstance(reservation_time, time) else str(reservation_time)
        except Exception as e:
            print(f"Error formatting date/time: {e}")
            formatted_date = str(reservation_date)  # Fallback to string
            formatted_time = str(reservation_time)  # Fallback to string
        
        print((reservation_id, member_id, section_id, formatted_date, formatted_time))

# Function to handle different menu options
def main():
    conn = get_connection()  # Connect to the database
    cursor = conn.cursor()

    while True:
        choice = display_menu()  # Display menu and get user choice
        
        if choice == "1":
            section_name = input("Enter section name: ")
            section = Section(None, section_name)  # Create new section object
            section.save(cursor)  # Save section to database
            conn.commit()

        elif choice == "2":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            mobile_phone = input("Enter mobile phone: ")
            age = int(input("Enter age: "))
            member = Member(first_name, last_name, email, mobile_phone, age)  # Create new member object
            member.save(cursor)  # Save member to database
            conn.commit()

        elif choice == "3":
            member_id = input("Enter member ID: ")
            section_id = input("Enter section ID: ")
            pack_type = input("Enter pack type (8-visit or 15-visit): ").strip()
            if pack_type not in ['8-visit', '15-visit']:
                print("Invalid pack type. Please choose either '8-visit' or '15-visit'.")
                continue
            subscription = SubscriptionPack(member_id, section_id, pack_type)  # Create new subscription object
            subscription.save(cursor)  # Save subscription to database
            conn.commit()

        elif choice == "4":
            member_id = input("Enter member ID: ")
            section_id = input("Enter section ID: ")
            reservation_date = input("Enter reservation date (YYYY-MM-DD): ")
            reservation_time = input("Enter reservation time (HH:MM:SS): ")
            
            cursor.execute('''SELECT subscription_id, remaining_visits FROM SubscriptionPacks
                              WHERE member_id = %s AND section_id = %s''', (member_id, section_id))
            subscriptions = cursor.fetchall()
            
            if not subscriptions:
                print("No active subscription for this member and section.")
                continue

            subscription_pack = SubscriptionPack(member_id, section_id, '8-visit')  # Create subscription object
            subscription_pack.check_remaining_visits(cursor)  # Check remaining visits
            
            reservation = Reservation(member_id, section_id, reservation_date, reservation_time)  # Create new reservation object
            reservation.save(cursor, subscription_pack)  # Save reservation to database
            conn.commit()

        elif choice == "5":
            member_id = input("Enter member ID to delete: ")
            Member.delete(cursor, member_id)  # Delete member and related data
            conn.commit()

        elif choice == "6":
            cursor.execute("SELECT * FROM Sections;")  # Fetch all sections
            sections = cursor.fetchall()
            for section in sections:
                print(section)

        elif choice == "7":
            cursor.execute("SELECT * FROM Members;")  # Fetch all members
            members = cursor.fetchall()
            for member in members:
                print(member)

        elif choice == "8":
            cursor.execute("SELECT * FROM SubscriptionPacks;")  # Fetch all subscriptions
            subscriptions = cursor.fetchall()
            for subscription in subscriptions:
                print(subscription)

        elif choice == "9":
            display_reservations(cursor)  # Display all reservations

        elif choice == "10":
            print("Exiting program...thank you!")
            break

        else:
            print("Invalid choice. Please try again.")

    cursor.close()  # Close cursor
    conn.close()  # Close database connection

if __name__ == "__main__":
    main()  # Run the main function
