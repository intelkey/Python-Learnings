'''35. Fake Login System (A2 – dictionary + string methods)
    Username and password verify.'''


database = {
    "usernames" : "passwords",
    "alice": "password123",
    "bob": "securePass456",
    "charlie": "mySecret789",
    "david": "qwerty2026",
    "emma": "letmein321",
    "wow": "1234",
    "frank": "sunshine999"
}

username = input("Write your username: " ).lower()
password = input("Write your password: " )

if username in database:

    if database[username] == password:
        print("access granted!!")

    else:
        print("wrong password")

else:
    print("access denied")
