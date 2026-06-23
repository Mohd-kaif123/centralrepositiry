import re

pattern=r"^(\+91)?+[6-9]\d{9}"
mobile_number="9146579748"

if re.match(pattern,mobile_number):
    print(f"{mobile_number} Number is Valid")
else:
    print(f"{mobile_number} Number is not Valid")
