

numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])


numbers[0] = "ten"
numbers[-1] = 1
shortened_numbers = numbers[2:]
check = 9 in numbers
print(check)
print(shortened_numbers)
print(numbers)

