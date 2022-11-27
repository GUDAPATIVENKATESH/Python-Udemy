# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
Name = (name1 + name2).lower()
T = Name.count("t")
R = Name.count("r")
U = Name.count("u")
E = Name.count("e")
L = Name.count("l")
O = Name.count("o")
V = Name.count("v")

Eurt = str(T+R+U+E)
Love = str(L+O+V+E)
Love_Score = int(Eurt + Love)
if Love_Score < 10 or Love_Score > 90 :
    print(f"Your score is {Love_Score}, you go together like coke and mentos.")
elif Love_Score < 40 and Love_Score > 50 :
    print(f"Your score is {Love_Score}, you are alright together.")
else :
    print(f"Your score is {Love_Score}.")

