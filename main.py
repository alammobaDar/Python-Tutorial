
students = (("Darren", 3.9, 18),
            ("Jonel", 3.9, 19),
            ("Dan", 3.5, 18),
            ("Luis", 4, 18),
            ("Rj", 4, 18),
            ("Tupe", 3.7, 18))
# students.sort()
# grade = lambda grades: grades[1]
age = lambda ages: ages[2]

# used a sort() method
# students.sort(key= age, reverse= True)


#used a sort() function
sorted_students = sorted(students, key= age)

for i in sorted_students:
    print(i)
