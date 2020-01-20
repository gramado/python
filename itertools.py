import itertools as it


def test(x):
    return x < 4


def main():
    nums = [2, 4, 9, 8, 15, 2, 1]
    ev = [2, 4, 6, 8]
    od = [1, 3, 5, 7]
    # Cycle: it cycles over given collection
    # cy = it.cycle(nums)
    # this loop causes an infinite loop coz there is no condition to stop it
    # and it'll will cycle whenever i is in cy
    # for i in cy:
    #     print(i)

    # Count: it counts from the given number increased by the second argument
    # co = it.count(0, 1)
    # print(next(co))
    # print(next(co))
    # print(next(co))

    # Accumulate: it accumulates the given collection
    # ac = it.accumulate(nums)
    # print(list(ac))

    # Chain: for connecting tow objects or collections
    # ch = list(it.chain(ev, od))
    # print(ch)

    # dropwhile and takewhile
    # nums = sorted(nums)
    # print(list(it.dropwhile(test, nums)))
    # print(list(it.takewhile(test, nums)))


if __name__ == '__main__':
    main()
