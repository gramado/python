def func(location, name='Shoukrey', job='Developer'):
    """ func(location, name=, job=) ==> just for testing keyword concept
    :param location: is required parameter
    :param name: is default parameter (you have to specify keyword)
    :param job: is default parameter (you have to specify keyword)
    :return: string that contains information of this project's author
    """
    return " ".join([name, job, location])


def func1(**info):
    for i in info.keys():
        print(f"{i}: {info[i]}")


# multiple(unlimited) arguments
def fun2(*args):
    for arg in args:
        print(arg)


def main():
    # ignoring default parameters and just type required params
    # print(func('Sudan'))

    # this will result in "Shoukrey Tom Developer Sudan"
    # print(func(name="Shoukrey Tom", location='Sudan'))

    # binding dictionary to the function
    info = {
        "author": "Shoukrey Tom",
        "job": "developer",
        "location": "Sudan"
    }
    func1(**info)

    # args = ["arg1", "arg2", "arg3", "arg4", "arg5"]
    # fun2(*args)
    # print("========================================")
    # fun2("arg1", "arg2", "arg3", "arg4", "arg5")

    # docstring
    # print(func.__doc__)

    # TODO: uncomment all comments


if __name__ == '__main__':
    main()
