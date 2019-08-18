for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

#######################################################

number_of_stars = int(input("No of times to repeat:"))
print('*' * number_of_stars)
print()

#######################################################

str = '*'
final_value = number_of_stars + 1

for i in range(1, final_value):
    print(str)
    str = str + '*'
