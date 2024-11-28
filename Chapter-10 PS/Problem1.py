class Programmer:
    company = "Microsoft"
    def __init__(self, name, pincode, salary):
        self.name = name
        self.pincode = pincode
        self.salary = salary

p1 = Programmer("Animesh", 123456, 1000000)
print(p1.name, p1.pincode, p1.salary, p1.company)
    