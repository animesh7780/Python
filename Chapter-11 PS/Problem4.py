class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
    
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
    
c1 = Complex(1, 2)
c2 = Complex(3, 4)
c3 = c1 + c2
print(c3.real, c3.imaginary)
print(c3)