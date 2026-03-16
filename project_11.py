'''11. Double Space Detector (A2 – find)
  Detect whether a sentence contains double spaces.'''

sentence = input("write your sentence:" )
detect = sentence.find("  ")
if detect == -1:
    print("there is no double space in your sentence")
else: 
    print("double space detected in your sentence")
