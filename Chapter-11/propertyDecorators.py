class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"the value of a is {cls.a}")
        
    @property
    def show(self):
        return self.ename
        
    @name.setter 
    def name (self, value):
        self.ename = value
        
e = Employee()
e.name = "Animesh"
e.a = 45
e.show()