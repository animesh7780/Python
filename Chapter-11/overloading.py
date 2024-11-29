class Number:
    def __init__(self, a):
        self.a = a
        
    def __add__(self, other):
        return self.a + other.a 
        
n = Number(10)
m = Number(20)

print(n + m)