# WAP for password validation using regular expression.
# 1. Atleast 8 characters
# 2. atleast one uppercase letter
# 3. atleast one lowercase letter
# 4. atleast one digit
# 5. atleast one special character(@#$%^&+=)
# 6. no whitespace allowed
import re
pattern=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=])(?=\S+$).{8,}$"

password= "Nikunj#$123"

if re.match(pattern,password):
    print("Password is valid.")
else:
    print("Password is invalid.")