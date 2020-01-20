def main():
    names = ["Shoukrey", "Harry", "Mohamed", "Mostafa"]
    jobs = ["Founder", "Manager", "Co-Founder", "Tester"]

    # using foreach technique
    # for name in names:
    #     print(name)

    # using for with range
    # for i in range(len(names)):
    #     print(names[i])

    # using iter built-in function
    # it = iter(names)
    # for i in it:
    #     print(i)

    # using enumerate built-in function
    # for i, n in enumerate(names, start=1):
    #     print(i, n)

    # using zip built-in function (mostly it's used when combining tow lists)
    # for i, m in zip(names, jobs):
    #     print(i, m)

    # using both zip & enumerate
    # for i, n in enumerate(zip(names, jobs), start=1):
    #     print(i, n[0], n[1])

    # print list in reversed way using built-in function reversed
    # for i, n in enumerate(zip(reversed(names), reversed(jobs)), start=1):
    #     print(i, n[0], n[1])

    # TODO: uncomment all above comments for testing
    # NOTE: there still more loop techniques not provided in this file.


if __name__ == '__main__':
    main()
