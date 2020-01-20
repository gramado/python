def main():
    names = ["name1", "name2", "name3"]
    #foreach loop
    for name in names:
        print(name)

    for i in range(0, 9, 2): #it will loop from 0 to 9 increased by 2
        print(i)

    i = 0
    while i != len(names):
        print(names[i])
        i+=1

if __name__ == "__main__":
    main()
