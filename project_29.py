'''
29. Student Ranking Generator (A2 – dictionary + sorting)
   By generating ranking from Marks dictionary .
'''

marks = {
    "Rohan" : 99,
    "Fang" : 89,
    "Harish" : 67,
    "Gautam" : 99.99,
    "Jagdesh" :33,
    "Sarru" : 70,
    "Praveen" : 100
}

values = list(marks.values())
values.sort()
values.reverse()

for m in values:
    for name in marks:
        if marks[name] == m:
            print(name, m)


