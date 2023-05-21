import serial
import csv

# Define the name of the CSV file
filename = "data.csv"

# Open the serial port
ser = serial.Serial('COM3', 9600) # Change COM3 According to the USB port you use

# Define the number of integers per row
int_per_row = 10

# Define a list to store the integers
int_list = []

# Loop to receive data and write it to the CSV file
while True:
    # Read an integer from the serial port
    data = int(ser.readline().decode().rstrip())

    # Add the integer to the list
    int_list.append(data)

    # If the list is full, write it to the CSV file and clear it
    if len(int_list) == int_per_row:
        # Open the CSV file and append the new row to the end
        with open(filename, 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(int_list)

        # Clear the list
        int_list = []