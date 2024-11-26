percentage = int(input("Enter grade: "))

if(percentage==100 and percentage>=90):
    print("A")
elif(percentage>=80 and percentage<90):
    print("B")
elif(percentage>=70 and percentage<80):
    print("C")
elif(percentage>=60 and percentage<70):
    print("D")
else:
    print("F")