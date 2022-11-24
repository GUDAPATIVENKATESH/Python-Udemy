#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome! to Tip Calculator")
Bill = float(input("What was the total Bill?\n:"))
Tip_Percent = float(input("What percentage tip would you like to give? 10,12 or 15?\n:"))
People = float(input("How meny people to split the Bill?\n:"))

Tip = Bill * (Tip_Percent / 100)
Total_Bill = round(Bill + Tip, 2)
Bill_per_person = round(Total_Bill / People, 2)
print(f"Your total Tip is ${Tip},total Bill including Tip was ${Total_Bill} and each should Pay ${Bill_per_person}")
print("Thanks")
