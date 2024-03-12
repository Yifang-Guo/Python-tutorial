band = {
    "vocal": "plant",
    "guitar": "page"
}

band2 = dict(vocal="plant", guitar="page")

print(band)
print(band2)
print(type(band))

#access items
print(band["vocal"])
print(band.get("guitar"))

#list all keys and values
print(band.keys())
print(band.values())

#list of key/value pairs as tuple
print(band.items())

#verify a key exists
print("guitar" in band)
print("triangle" in band)

#change values
band["vocal"] = "Tom"
band.update({"bass":"JPJ"})
print(band)

#remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())#tuple
print(band)

#delete and clear
band["drums"] = "Bonhan"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

#copy dictionary
band2 = band.copy()
band2["drum"] = "Dave"
print(band)
print(band2)

#or use dict constructor
band3 = dict(band)
print(band3)

#nested dictionaries
member1 = {
    "name": "Plane",
    "instrument": "vocals"
}

member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band4 = {
    "member1": member1,
    "member2": member2
}
print(band4)
print(band4["member1"]["name"])

#sets
nums = {1, 2, 3, 4, 4}

nums2 = set((1, 2, 3, 4, 5))

print(nums)
print(nums2)
print(type(nums))

nums3 = {1, True, 9, 2, False, 3, 4, 0}
print(nums3)

#check if a value in set
print(2 in nums3)

#add  a new element to a set
nums3.add(14)
print(nums3)

#add elements from one set to another set

nums4 = {5, 66, 89}
nums3.update(nums4)
print(nums3)

#merge two sets to create a new set
one = {1, 2, 3}
two = {2, 3, 4}
#myNewSet = one.union(two)
one.intersection_update(two)
print(one)

three = {1, 2, 3}
four = {2, 3, 4}
three.symmetric_difference_update(four)
print(three)