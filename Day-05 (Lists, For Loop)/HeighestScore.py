# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
Heighest_Score = 0

for score in student_scores :
  if score > Heighest_Score :
    Heighest_Score = score
print(f"The Heighest Score in the Class is {Heighest_Score}")