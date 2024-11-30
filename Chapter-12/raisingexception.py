a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

if(b==0):
    raise Exception("Cannot divide by zero")

else:
    print(a/b)