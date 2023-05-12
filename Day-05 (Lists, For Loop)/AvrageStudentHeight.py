# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
print(student_heights)
total_height = 0
for height in student_heights :
  total_height += height
print(f"Total Height: {total_height}")

Number_of_Students = 0
for student in student_heights:
  Number_of_Students += 1
print(f"Number of Students: {Number_of_Students}")

Average_Student_Height = round(total_height / Number_of_Students)
print(f"Average Height is {Average_Student_Height}")