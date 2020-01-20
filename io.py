def addition():
    try:
        x = int(input("Enter number1: "))
        y = int(input("Enter number2: "))
        print(f"{x} + {y} = {x+y}")
    except ValueError:
        print("please enter integer values")
        addition()

def concat():
    s1 = str(input("Enter frist name: "))
    s2 = str(input("Enter last name: "))
    s3 = s1 + " " + s2
    print(f"your name is {s3}")

def main():
    addition()
    concat()


if __name__ == "__main__":
    main()
