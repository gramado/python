def main():
    #list
    names = ["shoukry", "mohamed", "tom", "mubarak"]

    #tuple
    coordinate = (3.3, 1.5)

    #dictionary
    rank = {1: "Sudan", 2: "USA", 3: "India"}

    #set
    ids = set()
    ids.add(1)
    ids.add(2)
    ids.add(3)
    ids.add(1) #this one won't be added

    print(type(names))
    print(type(coordinate))
    print(type(rank))
    print(type(ids))

    print("======ids values======")
    for id in ids:
        print(id)

if __name__ == '__main__':
    main()
