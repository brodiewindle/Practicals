file = open('name.txt', 'w')
name = input("Please enter your name: ")
print(name, file=file)

print("your name is {:}".format(name))

file.close()

file = open("numbers.txt", "r")
number1 = int(file.readline())
number2 = int(file.readline())
file.close()
print(number1 + number2)


number_file = open('numbers.txt', 'r')

total = 0
for line in number_file:
    total = total + int(line)
number_file.close()
print(total)
