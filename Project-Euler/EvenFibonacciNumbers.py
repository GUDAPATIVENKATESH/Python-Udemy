# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, . . .
# By considering the terms in the Fibonacci sequence whose values do not exceed 
# four million, find the sum of the even-valued terms.

#for term in range(10) :
Number = [1, 2]
for r in range(10) :
    
    add = Number[len(Number) -1] + Number[len(Number) -2]
    print(add)
    Number.append(add)
print(Number)

# four million, find the sum of the even-valued terms.
# 4000000


