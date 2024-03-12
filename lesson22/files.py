import os
# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

f = open('lesson22/names.txt')
#print(f.read(14))

#print(f.readline())
#print(f.readline())


for lines in f:
    print(lines)

f.close()

try:
    f = open("lesson22/name_list.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exits")
finally:
    f.close()

#append - create a file if it doesn't exist
f = open("lesson22/names.txt", "a")
f.write("\nNeil")
f.close()

f = open("lesson22/names.txt")
print(f.read())
f.close()

# write (overwrite)
f = open("lesson22/context.txt", "w")
f.write("I deleted all of the context.")
f.close()

f = open("lesson22/context.txt")
print(f.read())
f.close()

# Two ways of create a new file

#open a file for writing, creates a file if it doesn't exist
f = open("lesson22/name_list.txt", "w")
f.close()

#create a specified file, but returns an error if the file exists
if not os.path.exists("lesson22/Dave.txt"):
    f = open("lesson22/Dave.txt", "x")
    f.close()

#delete a file
if os.path.exists("lesson22/Dave.txt"):
    os.remove("lesson22/Dave.txt")
else:
    print("The file you wish to delete does not exist")

with open("lesson22/more_names.txt") as f:
    content = f.read()

with open("lesson22/names.txt", "a") as f:
    f.write(content)