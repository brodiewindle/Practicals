

MIN_LENGTH = 2


def main():
    password = get_password(MIN_LENGTH)
    print_asterisks(password)

def get_password(MIN_LENGTH):

    password = input("Please enter a password at least {} characters long: ".format(MIN_LENGTH))

    while len(password) < MIN_LENGTH:
        print("Please enter a valid password!")
        password = input("Please enter a password at least {} characters long: ".format(MIN_LENGTH))
    return password

def print_asterisks(sequence):
    print(len(sequence)*'*')



main()
