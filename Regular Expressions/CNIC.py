import re

cnic = input("Enter your CNIC with dashes: ")
pattern = r'^[0-9]{5}-[0-9]{7}-[0-9]{1}$'

if re.search(pattern, cnic):
    print(cnic)
else:
    print("Invalid CNIC")