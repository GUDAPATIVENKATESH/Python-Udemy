# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143.
print("Welcome!. To prime factor calculator.")
Number = int(input("Enter the Number\n:"))
Factors = []
for num in range(2, Number) :
    if Number % num == 0 :
        Factors.append(num)
print(Factors)
print(f"the largest Factor for {Number} is {Factors[-1]}")
Prime_Factor = []
for item in Factors :
    