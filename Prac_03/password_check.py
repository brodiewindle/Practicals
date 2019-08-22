MIN_LENGTH = 2


def main():
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def get_password(min_length):
    password = input("Please enter a password at least {} characters long: ".format(MIN_LENGTH))

    while len(password) < min_length:
        print("Please enter a valid password!")
        password = input("Please enter a password at least {} characters long: ".format(MIN_LENGTH))
    return password


def print_asterisks(sequence):
    print(len(sequence) * '*')


main()
