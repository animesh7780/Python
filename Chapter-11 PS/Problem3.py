class Employee:
    salary = 23716
    increment =17
    
    @property
    def salaryOp(self):
        return self.salary+self.salary * (self.increment/100)
    
    @increment.setter
    def increment(self, salary):
        self.increment =  ((salary/self.salary)-1)*100
        
    
e =Employee()
print(e.salaryOp)