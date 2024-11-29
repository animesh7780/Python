class Animal:
    def __init__(self):
        print("Animal")

class Pets(Animal):
    def __init__(self):
        print("Keep at home")
    
class Dog(Pets):
    def bark(self):
        return "bark"
    
d = Dog()
print(d.bark())