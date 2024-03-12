def hello():
    print("hello world!")

hello()

def sum(num1, num2 = 3):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2

print(sum("a"))

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Dave", "John", "Tom")

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = "Dave", last = "Gray")