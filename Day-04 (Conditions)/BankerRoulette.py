# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random
# Choice = random.choice(names)
# print(Choice)
Number_of_names = len(names)
Choice = random.randint(0, Number_of_names - 1)
Person = names[Choice]
print(f"{Person} is going to buy the meal today!$")