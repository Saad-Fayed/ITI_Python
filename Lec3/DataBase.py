import csv

# Define the name of the CSV file
filename = "database.csv"

# Define List to for the field names 
fields = ["Name", "Address", "Phone Number", "Age"]

# Create the CSV file and write the field names to the first row
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)

# Function to add data to the CSV file
def add_data():
    # Ask the user for the data
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    phone = input("Enter Phone Number: ")
    age = input("Enter Age: ")

    # Open the CSV file and append the new data to the end
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([name, address, phone, age])
    print("Data added successfully!")

# Function to search the CSV file by name
def search_data():
    # Ask the user for the name to search
    name = input("Enter Name to search: ")

    # Open the CSV file and search for the name
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        # Skip the first row (which has the field names)
        next(csvreader)

        # Loop through the remaining rows and search for the name
        found = False
        for row in csvreader:
            if row[0] == name:
                # If the name is found, print the data and set found to True
                print("Name: ", row[0])
                print("Address: ", row[1])
                print("Phone Number: ", row[2])
                print("Age: ", row[3])
                found = True
                break

        # If the name is not found, print a message
        if not found:
            print("Name not found in the database.")

# Main function of the program
# Loop until the user chooses to quit
while True:
    print("\nWelcome to the database program!")
    print("1. Add Data")
    print("2. Search Data")
    print("3. Quit")

    # Ask the user for their choice
    choice = input("Enter your choice (1-3): ")

    # Call the appropriate function based on the user's choice
    if choice == "1":
        add_data()
    elif choice == "2":
        search_data()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
