# logic for leap year
# Year must be divisible by 4 and not divisible by 100 also divisible by 400
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0:
            print(f"{year} is a Leap year")
        else :
            print(f"{year} is Not a Leap year")
    else :
        print(f"{year} is a Leap year")
else :
    print(f"{year} is Not a Leap year")