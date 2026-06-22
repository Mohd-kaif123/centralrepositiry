import re
pattern=r"^[6-9]\d{9}$"
mobile_number="9546549748"
if re.match(pattern,mobile_number):
    print(f"{mobile_number} is a vaid mobile number")
else:
    print(f"{mobile_number} is not valid")