try:
    a = int(input("Enter first number :"))
    print(a)

except ValueError as v:
    print("Expecting a number", v)  
  

else:
    print("No exception")