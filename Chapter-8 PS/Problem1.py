a = int(input("Enter a number:"))
b = int(input("Enter another number:"))
c = int(input("Enter another number:"))

print("greatest of numners:", max(a,b,c))

def max(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c