'''
4. Email Validator (Basic) (A2 – string methods)
Check whether the email contains "@" and "." or not.
'''

email = input("Enter your email: ")
at = email.find("@") # Find the position of "@" in the email
dot = email.find(".") # Find the position of "." in the email
if at == -1 or dot == -1: # If "@" or "." is not found, the email is invalid
    print("Invalid Email: '@' and '.' are required in the email address.")
