person = "Dave"
coins = 3

print(person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left." % (person, coins)
print(message)

message = "\n{} has {} coins left.".format(person, coins)
print(message)

message = "\n{1} has {0} coins left.".format(coins, person)
print(message)

message = "\n{person} has {coins} coins left.".format(coins=coins, person=person)
print(message)


player = {'person': "Yifang", "coins": 6}
message = "\n{person} has {coins} coins left.".format(**player)
print(message)


#f-strings
message1 = f"\n{person} has {coins} left."
print(message1)

message1 = f"\n{person} has {2 * 10} left."
print(message1)

message1 = f"\n{person.lower()} has {coins} left."
print(message1)

message1 = f"\n{player['person']} has {coins} left."
print(message1)

#you can pass formatting options
num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")