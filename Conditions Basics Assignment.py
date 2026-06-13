Math_grade = float(input("Enter your Math grade: "))
Is_student_passed = print("Did you pass the Math class?", Math_grade >= 50)
Science_grade = float(input("Enter your Science grade: "))
Is_student_passed = print("Did you pass the Science class?", Science_grade >= 50)
History_grade = float(input("Enter your History grade: "))
Is_student_passed = print("Did you pass the  History class?", History_grade >= 50)
Geography_grade = float(input("Enter your Geography grade: "))
Is_student_passed = print("Did you pass the Geography class?", Geography_grade >= 50)
English_grade = float(input("Enter your English grade: "))
Is_student_passed = print("Did you pass the English class?", English_grade >= 50)

Average_grade = ((Math_grade + Science_grade + History_grade + Geography_grade + English_grade) / 5)

if Average_grade >= 85:
    print("Your average grade is Excellent")

if 75 <= Average_grade < 85:
    print("Your average grade is Very Good")  

if 65 <= Average_grade < 75:
    print("Your average grade is Good")

if 50 <= Average_grade < 65:
    print("Your average grade is Pass")

if Average_grade < 50: 
    print("Your average grade is Fail")

if (Average_grade >= 85 and Math_grade >= 80)  or (Average_grade < 85 and Math_grade >=90):
    print("You are eligible for joining the competetion")
else:
    print("You can't join the competetion!")

