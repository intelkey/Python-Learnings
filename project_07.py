'''7. Sentence Word Counter (A1→A2 – split)
Take a sentence as input from the user and print the number of words in it.
'''

sentence = input("Write your sentence: ")
words = sentence.split()
print("Word count:", len(words))
