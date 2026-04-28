'''27. Duplicate Number Finder (A2 – list + set)
   Detect duplicate numbers in the list.'''

n1 = int(input("write n1: " ))
n2 = int(input("write n2: " ))
n3 = int(input("write n3: " ))
n4 = int(input("write n4: " ))
n5 = int(input("write n5: " ))
n6 = int(input("write n6: " ))
n7 = int(input("write n7: " ))
n8 = int(input("write n8: " ))
n9 = int(input("write n9: " ))
n10 = int(input("write n10: " ))

our_list = [n1 , n2 ,n3, n4 , n5 ,n6, n7 , n8 ,n9, n10]

seen_numbers = set()
duplicates = set()

for number in our_list:
    if number in seen_numbers:
        duplicates.add(number)
    else:
        seen_numbers.add(number)

print("Duplicate numbers are:", duplicates)
        
