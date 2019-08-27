import random

MIN = 1
MAX = 45
NUMBERS_ON_EACH_LINE = 6

number_of_quick_picks = int(input("Please enter the number of quick picks: "))

if number_of_quick_picks <= 0:
    print("Choose a different number my dude")
    number_of_quick_picks = int(input("Please enter the number of quick picks: "))


for i in range(number_of_quick_picks):
    number = random.sample(range(MIN, MAX), k=6)
    number.sort()
    print(" ".join(map(str, number)))
