first = "Yifang"
last = "Guo"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

#constructor
pizza = str("pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

#concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

#casting a number to a string
decade = str(10)
print(type(decade))
print(decade)

statement = "YOLO" + decade + "s."
print(statement)

#multiple lines
multiline = '''
hey, how are you?

I was just checking in.

            all good?

'''
print(multiline)

#escaping special characters
sentence = 'I\'m a good student!\tHey!\n\nWhere are you?'
print(sentence)

#string methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "        "
multiline =  "       " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("-----")
#build a menu
title = "menu".upper()
print(title.center(20, '*'))
print("coffee".ljust(16, ".") + "$3".rjust(4, "."))
print("Muffin".ljust(16, ".") + "$2".rjust(4, "."))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4, "."))

print("-----")
#string index values
print(first[0])
print(first[1:])

#some methods return boolean data
print(first.endswith("Z"))

#boolean data type
myValue = True
x = bool(False)
print(type(x))
print(isinstance(myValue, bool))

#numeric data types

#integer
price = 100
best_price = int(20)
print(type(price))
print(isinstance(best_price, int))

#float type
gpa = 4.00
y = float(3.98)
print(type(gpa))
print(isinstance(y, float))

#complex type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

#built-in functions for numbers
print(abs(gpa))
print(round(y, 1))

import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(y))

#casting a string to a number
zipcode = "300191"
zip_value = int(zipcode)
print(type(zip_value))