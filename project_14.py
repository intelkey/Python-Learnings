'''14. Palindrome Checker (A2 – slicing comparison)
    Check if the word is a palindrome or not.'''

word = input("write a word:" ).lower()
reversed_word = word[::-1]

if word == reversed_word:
    print("This is a palindrome")
else:
    print("This is not a palindrome")
