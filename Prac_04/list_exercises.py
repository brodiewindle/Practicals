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

# Ask the user for their username. If the username is in the above list of authorised users, print "Access granted",
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user = input("Please enter your username: ")

access = user in usernames
if access == True:
    print("Access Granted")
else:
    print("Access Denied")
