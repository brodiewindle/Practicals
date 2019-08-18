"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
"""
sales = float(input("Enter sales: $"))

if sales >= 1000:
    bonus = sales * 0.15
    print("Your bonus will be ${:.2f}".format(bonus))
elif 0 > sales < 1000:
    bonus = sales * 0.1
    print("Your bonus will be ${:.2f}".format(bonus))
else:
    print("Error, please enter a value greater than zero!")
"""
######################################################################3

sales = float(input("Enter sales: $"))

while sales >= 0:

    if sales >= 1000:
        bonus = sales * 0.15
    else:
        bonus = sales * 0.1
    print("Your bonus will be ${:.2f}".format(bonus))
    sales = float(input("Enter sales: $"))

print("Invalid Entry, please use a value greater than zero")
