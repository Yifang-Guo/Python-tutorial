value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# while value <= 10:
    
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("loop ends at " + str(value))

names = ["Dave", "john", "Sara", "Tom"]

# for x in names:
#     if x == "Sara":
#         break
#     print(x)

# for x in range(2,4):
#     print(x)
for x in range(0, 100, 15):
    print(x)
else:
    print("glad that\'s over")

actions = ["code", "eat", "sleep"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")