class Employee:
    language = "Python"
    salary = 2891471283
    
    def getInfo(self):
        print(self.language, self.salary)
    
    @staticmethod
    def greet():
        print("Hello")
    
animesh = Employee()
# print(animesh.language, animesh.salary)

harry = Employee()
harry.name = "Harry"
# print(harry.name, harry.language, harry.salary)
Employee.greet()
Employee.getInfo(animesh)

# name is object attribute and salary and language is class attribute