class calculator:
    def __init__(self, num):
        self.num = num
        
    @staticmethod
    def greet():
        print("Hello")
    def square(self):
        return self.num * self.num
    def cube(self):
        return self.num * self.num * self.num
    def squareRoot(self):
        return self.num ** 0.5
        
a = calculator(10)
a.greet()
print(a.square())
print(a.cube()) 
print(a.squareRoot())