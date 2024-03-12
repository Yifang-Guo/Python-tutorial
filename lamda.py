squared = lambda num : num * num

print(squared(4))

addTwo = lambda num : num + 2

print(addTwo(8))

sum = lambda a, b : a + b

print(sum(5, 5))

#########
def funcBuilder(x):
    return lambda  num : num + x

addTen = funcBuilder(10)
print(addTen(23))

#########


numbers = [3, 78, 6, 99, 45, 21]

squaredNum = map(lambda num : num * num, numbers)

print(list(squaredNum))
print(list(numbers))

##########

evenNum = filter(lambda num : num % 2 == 0, numbers)
print(list(evenNum))

from functools import reduce



numbers1 = [1, 4, 6, 7, 9, 10]

total = reduce(lambda acc, curr : acc + curr, numbers1)

print(total)




names = ["Dave", "Yifang", "Tom", "John Jacob"]

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)

print(char_count)