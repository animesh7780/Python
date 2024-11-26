mark1 = int(input("Enter marks:"))
mark2 = int(input("Enter marks:"))
mark3 = int(input("Enter marks:"))


if((mark1+mark2+mark3)/3 >= 40):
    if(mark1 and mark2 and mark3 >= 33):
        print("Pass")
    else:
        print("Fail")
else:
    print("Fail")