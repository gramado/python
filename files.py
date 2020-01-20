import os

def create_file():
    names = ["name1", "name2", "name3", "name4"]
    #this is for windows os
    homeFolder = os.getenv("USERPROFILE")
    file_name = homeFolder+"\\Desktop\\file.txt"
    """File flags:
    1- a: for append
    2- r: for read-only
    3- w: for write-only
    you can combine those flags according to your needs
    """
    file = open(file_name, "a+")
    for name in names:
        file.write(name+"\n")


def read_file():
    #this is for windows os
    homeFolder = os.getenv("USERPROFILE")
    file_name = homeFolder+"\\Desktop\\file.txt"
    file = open(file_name, "r+")
    print(file.read())

def main():
    create_file()
    read_file()

if __name__ == "__main__":
    main()
