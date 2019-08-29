import random

MIN = 1
MAX = 45
NUMBERS_ON_EACH_LINE = 6

number_of_quick_picks = int(input("Please enter the number of quick picks: "))

if number_of_quick_picks <= 0:
    print("Choose a different number my dude")
    number_of_quick_picks = int(input("Please enter the number of quick picks: "))


for i in range(number_of_quick_picks):
    quick_pick = []
    for j in range(NUMBERS_ON_EACH_LINE):
        number = random.randint(MIN, MAX)
        while number in quick_pick:
            number = random.randint(MIN, MAX)
        quick_pick.append(number)
        quick_pick.sort()
    print(" ".join("{: 3}".format(number) for number in quick_pick))

