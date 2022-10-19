# This is a sample Python script.
from Student import Student
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

student1 = Student("Jamal","Aerospace Engineering", 3.9)
student2 = Student("Tiffany","Computer Science", 4.0)
student3 = Student("Jake","Remedial Studies", 0.5)

print(student1.on_honor_roll())
if student1.on_honor_roll() == 1: #using boolean logic; 1 = True
    print(str(student1.name) + ' is on honor roll.')

else:
    print(str(student1.name) + ' is not on honor roll.')

print(student3.on_honor_roll())
if student3.on_honor_roll() == 1: #using boolean logic; 1 = True
    print(str(student3.name) + ' is on honor roll.')
else:
    print(str(student3.name) + ' is not on honor roll.')