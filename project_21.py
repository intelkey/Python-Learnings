'''22. Duplicate Word Remover (A2 – set)
   Remove duplicate words in the sentence.'''

sentence = input("Write your sentence: ")

splitting = sentence.split()
unique_sentence = set(splitting)

result = " ".join(unique_sentence)
print(result)
