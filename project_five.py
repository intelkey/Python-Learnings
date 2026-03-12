'''5. Password Strength Checker (A2 – string validation)
Check if the password contains letters, numbers, and meets the required length.'''

assword = input("Write your password: ")

has_letter = False
has_digit = False

for ch in password:
    if ch.isalpha():
        has_letter = True
    if ch.isdigit():
        has_digit = True

if len(password) < 8:
    print("Password must be at least 8 characters long")

elif has_letter == False:
    print("Password must contain at least one letter")

elif has_digit == False:
    print("Password must contain at least one digit")

else:
    print("Strong password")
