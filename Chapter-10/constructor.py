class Employee:
    language = "Python"
    salary = 2891471283
    
    def __init__(self, name, salary, language): #dunder method
        self.name = name
        self.salary = salary
        self.language = language
    
    def getInfo(self):
        print(self.language, self.salary)
    
    @staticmethod
    def greet():
        print("Hello")
    
animesh = Employee("Animesh", 2891471283, "English")
print(animesh.name, animesh.language, animesh.salary)

#rohan = Employee()
