from Prac_06.guitars import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2012, 15000)

    print("{} is {} years old, Expected {}".format(gibson.name, gibson.get_age(), 97))
    print("{} to being vintage - Expected {}".format(gibson.is_vintage(), True))

    print("{} is {} years old, Expected {}".format(another.name, another.get_age(), 7))
    print("{} to being vintage - Expected {}".format(another.is_vintage(), False))

main()
