f = open("file.txt")
print(f.read())
f.close()

#the same can be written as

with open("file.txt") as f:
    print(f.read())