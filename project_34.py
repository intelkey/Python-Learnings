'''34. Email Username Extractor (A2 – string slicing + find)
    By extracting username from email address.'''

email = input("Write your email address: " )

checker = email.find("@")

if checker == -1:
    print("Email is not valid")
else:
    username = email[0:checker]
    print(username)


