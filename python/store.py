def main():

    #Function to delete an album from 'recordList'
    def delete_album(recordList, keyword):
        deleted = False
        updated_records = []
        #Iterating through each album in 'recordList'
        for album in recordList:
            #Checking if the keyword exists in any part of the album information
            if keyword in album:
                #Remove the album from the list if the keyword is found
                recordList.remove(album)
                deleted = True
            else:
                #Adding the album to 'updated_records' if keyword is not found
                updated_records.append(album)

        #If any album was deleted, update 'store.txt' file
        if deleted:
            # Update file with the remaining records. NOTE: the 'with open' statement
            # means that we don't have to add a 'file.close()' function
            with open("store.txt", "w") as file:
                for album in updated_records:
                    file.write(",".join(map(str, album)) + "\n")

        return deleted

    try:
        #A 'try-except' statement. Requested file might be accidentally deleted
        #so, an error will occur when asking for the specific file

        #Attempting to open file for reading
        f = open("store.txt","r")
        #Initialize music albums list
        recordList = []
        line = f.readline()
        #Read and append each line to 'recordList'
        while line:
            recordList.append(line.rstrip("\n").split(","))
            line = f.readline()
        f.close() #Closing file after reading
    except FileNotFoundError:
        print("The 'store.txt' file was not found")
        print("Begin with a new albums list")
        #Initializing empty albums list
        recordList = []

    choice = 0
    #Loop for displaying options menu until user chooses to exit
    while (choice != 5):
        print("=====THE BEST METAL ALBUMS STORE=====")
        print("1.Add an album")
        print("2.Search for an album")
        print("3.Display albums")
        print("4.Delete an album")
        print("5.Exit")
        choice = int(input("Please, select an option: "))

        #Option 1: Adding an album
        if choice == 1:
            print("Adding an album...")
            nAlbum = input("Enter the name of the album: ")
            nBand = input("Enter the name of the band: ")
            nOrigin = input("Enter the origin of the band: ")
            nYear = int(input("Enter release year of album: "))
            nProducer = input("Enter the name of the producer: ")
            nDuration = float(input("Enter the album duration (minutes): "))
            #Appending new album to 'recordList'
            recordList.append([nAlbum,nBand,nOrigin,nYear,nProducer,nDuration])

        #Option 2: Searching for an album
        elif choice == 2:
            print("Looking up for album...")
            keyword = input("Enter Search Term: ")
            found = False
            #Iterating through each album in 'recordList' to find matching keyword
            for album in recordList:
                if keyword in album:
                    print(album)
                    found = True
            if not found:
                print("Album not found")

        #Option 3: Displaying albums
        elif choice == 3:
            if not recordList:
                print("There are no albums to display")
            else:
                for i in recordList:
                    print(i)

        #Option 4: Deleting an album
        elif choice == 4:
            print("Looking up for album...")
            keyword = input("Enter Search Term: ")
            if delete_album(recordList,keyword):
                print("Album record deleted successfully")
            else:
                print("Album not found")
        #Exiting the program
        elif choice == 5:
            print("Goodbye!")
    print("Exiting application")

    #Saving records/data to a file
    file = open("store.txt","w")
    for album in recordList:
        file.write(",".join(map(str,album)) + "\n")
    file.close() #Closing file after writing

#Calling the 'main()' function
if __name__=="__main__":
    main()