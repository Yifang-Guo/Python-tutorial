name = "Dave"

# def  greeting(name):
#     color = "blue"
#     print(color)
#     print(name)

# greeting("John")

# def another():
#     greeting(name)

count = 1

def another():
    color = "blue"
    global count
    count += 1
    print(count)

    def greeting(name):
        print(color)
        print(name)

    greeting("Tom")

another()
print(count)