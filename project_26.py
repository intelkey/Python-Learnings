'''26. Word Frequency Counter (A2 – dictionary counting)
    Store the frequency of the words in the sentence in a dictionary.'''
    

sent = input("Write your sentence: ")
split_sent = sent.split()

freq = {}

for w in split_sent:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

print(freq)
