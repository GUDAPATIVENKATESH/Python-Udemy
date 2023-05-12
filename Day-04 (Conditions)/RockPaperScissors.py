rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

Computer_Choice = random.randint(0, 2)
print("Welcome to FunZone. Now you are playing Rock Paper Scissors. ")
print("Enter '0' for 'Rock', '1' for 'Paper' and '2' for 'Scissors'.")
Your_Choice = int(input("Enter your choice: "))
if Your_Choice >= 3 or Your_Choice < 0 :
    print("You entered an Invalid Option. You Lose!")
else:
  Game_Image = [rock, paper, scissors]
  print(f"You Chose{Game_Image[Your_Choice]}")
  print(f"Computer Chose {Game_Image[Computer_Choice]}")


  if Computer_Choice == Your_Choice :
    print("It's a Draw!")

  elif Computer_Choice == 2 and Your_Choice == 0 :
    print("You Win!")
  elif Computer_Choice > Your_Choice :
    print("You Lose!")
  elif Computer_Choice == 0 and Your_Choice == 2 :
    print("You Lose")
  elif Computer_Choice == 1 and Your_Choice == 2 :
    print("You Win")
  elif Computer_Choice == 0 and Your_Choice == 1 :
    print("You Win")