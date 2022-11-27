print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
Bill = 0
if height > 120 :
    Age = int(input("Enter Your Age\n:"))
    if Age < 12 :
        Bill += 5
    elif Age < 18 :
        Bill += 7
    elif Age >= 45 and Age <= 55 :
        Bill = 0
        print("Don't Worry Everything Will Be Allright!, Enjoy the Free Ride.")
    else :
        Bill += 12
    print(f"Your Bill for RollerCoaster Ride is ${Bill}")    
else :
    print("You can't ride because your Height is less then 120CM.")