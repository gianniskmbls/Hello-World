# Letter Appearance Statistics Program
# This program reads the contents of a text file, calculates the appearance statistics for each letter,
# and displays the results in descending order by count.
def calculate_letter_statistics(text):
    letter_stats = {}  # Dictionary to store letter appearance statistics

    # Iterate through each character in the text
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            char = char.lower()  # Convert the letter to lowercase for consistent counting

            # Check if the letter is already in the letter_stats dictionary
            if char in letter_stats:
                letter_stats[char] += 1 # Increment the appearance count
            else:
                letter_stats[char] = 1 # Initialize the appearance count

    return letter_stats

def main():
    file_path = 'hello.txt'  # Replace with the actual path of your text file

    try:
        # Open the file for reading
        with open(file_path, 'r') as file:
            text = file.read()

            # Calculate letter statistics using the calculate_letter_statistics function
            letter_statistics = calculate_letter_statistics(text)

            # Display the letter appearance statistics in descending order by count
            print("Letter Appearance Statistics (Descending Order by Count):")

            # Sort the letter statistics dictionary items by count in descending order
            sorted_stats = sorted(letter_statistics.items(), key=lambda x: x[1], reverse=True)

            # Iterate through sorted statistics and print the results
            for letter, count in sorted_stats:
                appearance = "appearance" if count == 1 else "appearances"
                print(f"'{letter}': {count} {appearance}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the file is properly closed after processing
        if file and not file.closed:
            file.close()

if __name__  == "__main__":
    main()

