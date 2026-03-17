'''20. List Element Remover (A2 – remove/pop)
   Give the user the option to remove an element from the list.'''


Element_one = int(input("Type the element one:" ))
Element_two = int(input("Type the element two:" ))
Element_three = int(input("Type the element three:" ))
Element_four = int(input("Type the element four:" ))
Element_five = int(input("Type the element five:" ))

The_list = [Element_one, Element_two, Element_three, Element_four, Element_five ]
print("This is your list:", The_list)

var = int(input("If you want to remove a number in your list then type the number:" ))
The_list.remove(var)
print("The final list:", The_list)
