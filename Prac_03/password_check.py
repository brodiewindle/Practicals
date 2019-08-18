print(len(password) * '*')


def main():
    MIN_LENGTH = 2

    password = input("Please enter a password at least {} characters long: ".format(MIN_LENGTH))

    while len(password) < MIN_LENGTH:
        password = input("Please enter a password at least {} characters long: ".format(MIN_LENGTH))



main()
