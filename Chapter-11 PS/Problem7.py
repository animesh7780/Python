class Vector:
    def __init__(self, x):
        self.x =x
        
    def __len__(self):
        return len(self.x)
    
v1 = Vector([1])
print(len(v1))