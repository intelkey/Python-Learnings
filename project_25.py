'''25. Contact Book Creator (A2 – dictionary store)
   Name aur phone number dictionary me store karo.'''

my_dict = {}

print("write first member info")
name1 = input("write your name: " )
num1 = int(input("write your num: " ))
my_dict[name1] = num1

print("write second member info")
name2 = input("write your name: " )
num2 = int(input("write your num: " ))
my_dict[name2] = num2

print("write third member info")
name3 = input("write your name: " )
num3 = int(input("write your num: " ))
my_dict[name3] = num3

print(str(my_dict).replace(", ", "\n"))
