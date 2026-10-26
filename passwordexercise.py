password= input("Enter your password: ")
#Check each requirement for a valid password 
length = len(password) >= 8
upper=any(char.isupper() for char in password)
lower=any(char.islower() for char in password)
digit=any(char.isdigit() for char in password)
special=any(char in "!@#$%^&" for char in password)
#Check if all requirements are met
if length and upper and lower and digit and special:
    print("Password is valid.")
else:
    print("Password is invalid.")
    if not length: 
        print("Password must be at least 8 characters.")
    if not upper:
        print("Password must have at least one uppercase letter.")
    if not lower:
        print("Password must have at least one lowercase letter.") 
    if not digit:
        print("Password must have at least one digit.")      
    if not special:
        print("Password must have at least one special character (!@#$%^&).")          