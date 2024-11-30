def main():
    try:
        a = int(input("Enter first number :"))
        print(a)
        return

    except ValueError as v:
        print("Expecting a number", v)  
        return

    finally:
        print("End of program")
        
main()