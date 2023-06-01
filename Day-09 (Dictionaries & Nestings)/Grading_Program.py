student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
# This is the scoring criteria:

# Scores 91 - 100: Grade = "Outstanding"

# Scores 81 - 90: Grade = "Exceeds Expectations"

# Scores 71 - 80: Grade = "Acceptable"

# Scores 70 or lower: Grade = "Fail"
Grades = ["Outstanding", "Exceeds Expectations", "Acceptable", "Fail"]
for student in student_scores :
    if student_scores[student] > 90 :
        student_grades[student] = Grades[0]
    elif student_scores[student] > 80 :
        student_grades[student] = Grades[1]
    elif student_scores[student] > 70 :
        student_grades[student] = Grades[2]
    else :
        student_grades[student] = Grades[3]

# 🚨 Don't change the code below 👇
print(student_grades)