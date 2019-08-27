


print("Please enter 5 numbers")

no1 = int(input("Number 1: "))
no2 = int(input("Number 2: "))
no3 = int(input("Number 3: "))
no4 = int(input("Number 4: "))
no5 = int(input("Number 5: "))

numbers = [no1, no2, no3, no4, no5]
print(numbers)


print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))

