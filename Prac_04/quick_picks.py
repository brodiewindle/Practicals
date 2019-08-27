import random

number_of_quick_picks = int(input("Please enter the number of quick picks: "))

if number_of_quick_picks <= 0:
    print("Choose a different number my dude")
    number_of_quick_picks = int(input("Please enter the number of quick picks: "))






for i in range(number_of_quick_picks):
    number = random.sample(range(45), k=6)
    print(number)
