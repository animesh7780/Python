a = str(input("Enter the name:"))
b = int(input("Enter the marks:"))
c = str(input("Enter the phone number:"))

display = "{a} scored {b} marks and his phone number is {c}".format(a=a, b=b, c=c)
print(display)