import os


def main():
    os.chdir('FilesToSort')
    category_extension = {}
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        filename_extension = filename.split('.')[-1]
        if filename_extension not in category_extension:
            category = input("What category would you like to sort {} files into? ".format(filename_extension))
            category_extension[filename_extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
        os.rename(filename, "{}/{}".format(category_extension[filename_extension], filename))


main()
