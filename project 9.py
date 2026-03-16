'''9. Username Generator (A2 – slicing)
   Generate a username from the user's first name and last name.'''

print("Hey there! this is a username generator tool")

first_name = input("write your first name:" )
last_name = input("write your last name:" )

print(first_name[0:3] + last_name[0:3].lower())

