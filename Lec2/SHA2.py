# import hashing library
import hashlib

while True:
    #ask user to enter Str he want to Hash
    data = input("Enter the Data you want to Hash : ")

    #Transform String from Askii to Bytes
    encoded_data = data.encode()  #utf-8

    #Generate hashed Hex Array
    str_hashed = hashlib.sha256(encoded_data)

    #Transform the Hex array to Askii
    str_hex = str_hashed.hexdigest()

    print(str_hex)