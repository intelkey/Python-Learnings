'''18. Marks Analyzer (A2 – list)
   Take student marks as input and print the highest, lowest, and average marks.'''


student_1 = int(input("write marks of student one:" ))
student_2 = int(input("write marks of student two:" ))
student_3 = int(input("write marks of student three:" ))
student_4 = int(input("write marks of student four:" ))
student_5 = int(input("write marks of student five:" ))
student_6 = int(input("write marks of student six:" ))
student_7 = int(input("write marks of student seven:" ))
student_8 = int(input("write marks of student eight:" ))
student_9 = int(input("write marks of student nine:" ))
student_10 = int(input("write marks of student ten:" ))

marks_list = [student_1, student_2, student_3, student_4, student_5, student_6, student_7, student_8, student_9, student_10 ]

print(max(marks_list))
print(min(marks_list))
total = sum(marks_list)
average = total / len(marks_list)
print(average)
