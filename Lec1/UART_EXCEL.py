import serial
import pandas as pd

# Configure the serial port
ser = serial.Serial('COM1', 9600)  # Replace 'COM1' with the name of your serial port
ser.flushInput()

# Read data from the serial port
data = []
while True:
    try:
        line = ser.readline().decode('utf-8').rstrip()
        data.append(line)
    except KeyboardInterrupt:
        break

# Write the data to an Excel sheet
df = pd.DataFrame(data, columns=['Data'])
df.to_excel('output.xlsx', index=False)
print('Data written to output.xlsx')

