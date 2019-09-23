from Prac_06.guitars import Guitar

guitars = []

print("My guitars!")

name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    add_guitar = Guitar(name, year, cost)
    guitars.append(add_guitar)
    print("{} ({}) : ${} added.".format(add_guitar.name, add_guitar.year, add_guitar.cost))
    name = input("Name: ")

if guitars:
    guitars.sort()
    print("These are my guitars: ")
    for i, guitar in enumerate(guitars):
        vintage_str = ""
        if guitar.is_vintage():
            vintage_str = "(vintage)"
        print("Guitar {}: {:20} ({}), worth ${:,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                vintage_str))
