'''2. Username Cleaner Tool (A2 – strip + lower + validation)
Clean the user’s input username: remove extra spaces, convert it to lowercase, and validate it.'''


username = input("write your username ", ).strip().lower() # cleaned complete
# now set some conditions
if not username:
    print("Username cannot be empty") 

elif len(username) < 3:
    print("Too short username it's not valid")

elif not username.isalnum():
    print("Only letters and numbers allowed")

else:
    print("This is a Valid username")
