from string import Template


def main():
    # using format flag
    author = "Shoukrey Tom"
    year = "2020"
    info1 = f"This project is created by {author} in {year}"
    print("info1: ", info1)
    # using format method
    info2 = "This project is created by {0} in {1}".format("Shoukrey Tom", "2020")
    print("info2: ", info2)
    # using template
    temp = Template("This project is created by ${author} in ${year}")
    info3 = temp.substitute(author="Shoukrey Tom", year="2020")
    print("info3: ", info3)
    # template with dictionary
    data = {
        "author": "Shoukrey Tom",
        "year": "2020"
    }
    info4 = temp.substitute(data)
    print("info4: ", info4)


if __name__ == '__main__':
    main()
