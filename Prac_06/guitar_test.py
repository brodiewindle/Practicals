from Prac_06.guitars import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2012, 15000)

    guitars = [gibson, another]
    for guitar in guitars:
        print("{} years old".format(guitar.get_age()))
        print("{} to being vintage".format(guitar.is_vintage()))


main()
