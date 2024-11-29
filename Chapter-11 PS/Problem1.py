class twodvector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
        
class threedvector(twodvector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    def show(self):
        print(self.x, self.y, self.z)
        
o = twodvector(1, 2)
o.show()
o = threedvector(1, 2, 3)
o.show()