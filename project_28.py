'''28. Username Availability Checker (A2 – list search)
    Check whether the username is available in the list.'''

names_list = ["sam", "rohan", "mikasa", "monu pradhan", "etc"]

write_name = input("write the name: ")

if write_name in names_list:
    print("name is NOT available (already taken)")
else:
    print("name is available")
