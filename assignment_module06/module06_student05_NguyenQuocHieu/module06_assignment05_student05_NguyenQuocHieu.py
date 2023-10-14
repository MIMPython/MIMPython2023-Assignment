import os


def iterate(folder: str):
    if os.path.isdir(folder):
        for element in os.listdir(folder):
            path = os.path.join(folder, element)
            if os.path.isdir(path):
                print("-object " + element + ", type folder")
            if os.path.isfile(path):
                print("-object " + element + ", type file")
    else:
        print(folder + "is not a folder")
        exit(1)


if __name__ == "__main__":
    iterate(r"C:\Users\scien\OneDrive\Pictures")
