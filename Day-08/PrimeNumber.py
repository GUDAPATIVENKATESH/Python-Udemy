#Write your code below this line 👇
import math
def prime_checker(number) :
    is_prime = True
    for r in range(2, number):
        if number % r == 0 :
            is_prime = False
            
    if is_prime == True :
        print(f"{number} is a prime nummber")
    else :
        print(f"{number} is not prime") 
                
            

    




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

