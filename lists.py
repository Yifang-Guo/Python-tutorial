users = ['yifang', 'tom', 'sara']

data = ['dave', 42, True]

emptyList = []

print("dave" in data)

print(users[0])
print(users[-3])
print(users.index('sara'))
print(data[0:2])
print(data[0:])

print(len(data))

users.append('Elsa')
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Bob')
print(users)

users[2:2] = ['Eddie', 'Alex']
print(users)


users[1:3] = ['heihei', 'haha', 'awesome']
print(users)

users.remove('heihei')
print(users)

print(users.pop())

del users[0]
print(users)

data.clear()
print(data)

users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 5, 12,4, 89, 5]
nums.reverse()
print(nums)

anothertuple = (1, 4, 2, 8)
(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)