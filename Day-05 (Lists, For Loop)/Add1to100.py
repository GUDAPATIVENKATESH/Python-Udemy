range_of_numbers = input("Enter the range of numbers you to add: ").split()
for number in range(0, len(range_of_numbers) ) :
    range_of_numbers[number] = int(range_of_numbers[number])
print(f"range {range_of_numbers}")

Sum = 0
for number in range(range_of_numbers[0], range_of_numbers[1]) :
    Sum += number
print(Sum)