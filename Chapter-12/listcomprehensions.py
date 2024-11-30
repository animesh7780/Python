mylist = [21,1,23,1,2,22,334]

squaredList = []

for item in mylist:
    squaredList.append(item**2)

print(squaredList)

# list comprhension

squaredList = [item**2 for item in mylist]
print(squaredList)