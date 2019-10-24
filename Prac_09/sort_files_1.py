import os


def main():
    os.chdir("FilesToSort")

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        folder_name = filename.split('.')[-1]
        try:
            os.mkdir(folder_name)
        except FileExistsError:
            pass
        print("{}/{}".format(folder_name, filename))
        os.rename(filename, "{}/{}".format(folder_name, filename))
        # shutil.move(filename, folder_name)


main()
