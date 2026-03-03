import re

email = input("Enter Gmail: ")

pattern = r'^[a-z0-9]+(\.[a-z0-9]+)*@gmail\.com$'

if re.fullmatch(pattern, email, re.IGNORECASE):
    print("Valid Gmail")
else:
    print("Invalid Gmail")