"""this is code that makes a shop calculator.
the user will assign a number of items to which
they will then be prompted to insert the price of each one """

# number_of_items = int(input("How many items do you have? "))
# array = []


# for i in range(0, number_of_items):
#     item_price = float(input("What is the price of the item? "))
#     array.append(item_price)
#
# total_price = sum(array)
# print("The total price is ${:.2f}".format(total_price))

number_of_items = int(input("How many items do you have? "))
total = 0

while number_of_items < 0:
    print("invalid entry")
    number_of_items = int(input("How many items do you have? "))

for i in range(0, number_of_items):
    item_price = float(input("What is the price of the item? "))
    total = item_price + total
if total > 100:
    total = 0.9 * total


print("The total price is ${:.2f}".format(total))
