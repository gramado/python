def to_lower(x):
    if x.isupper():
        return False
    return True


def to_upper(x):
    if x.islower():
        return False
    return True


def even_nums(x):
    if x % 2 == 0:
        return True
    return False


def squires(x):
    return x**2


def to_grade(x):
    if 90 <= x <= 100:
        return "A"
    elif 80 <= x < 90:
        return "B"
    elif 70 <= x < 80:
        return "C"
    elif 50 <= x < 70:
        return "D"
    return "F"


def main():
    nums = [1, 3, 8, 10, 7, 15]
    marks = [70, 93, 91, 80, 40, 50, 67, 83, 30]
    chars = "aBdEkeGlnMszX"

    # using filter to get upper-letters just from chars
    char_list1 = list(filter(to_upper, chars))
    print(char_list1)

    # using filter to get lower-letters just from chars
    char_list2 = list(filter(to_lower, chars))
    print(char_list2)

    # using filter
    num_list = list(filter(even_nums, nums))
    print(num_list)

    # using map to evaluate marks
    marks = sorted(marks)  # this is used for sorting lists
    grades = list(map(to_grade, marks))
    print(grades)

    # using map to squire nums values
    num_list2 = list(map(squires, nums))
    print(num_list2)


if __name__ == '__main__':
    main()
