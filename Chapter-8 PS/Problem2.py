def temp(c):
    f = c * 9/5 + 32
    return f

c = int(input("Enter temperature in celsius: "))

print("Temperature in farenheit:", temp(c))