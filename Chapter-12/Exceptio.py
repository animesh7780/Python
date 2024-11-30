try:
    a = int(input("Enter first number :"))
    print(a)

except ValueError as v:
    print("Expecting a number", v)  
  
except Exception as e:
    print("Expecting a number check input", e)
    
