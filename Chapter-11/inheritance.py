class Employee:
    company = "Google"
    def show(self):
        print(f"the name is{self.name} and salary is {self.salary}")
        
# class Programmer:
#         company = "Google1"
#         def show(self):
#             print(f"the name is{self.name} and salary is {self.salary}")
        
#         def showLanguage(self):
#             print(f"the programmer is fluent in {self.language}")
        
        
class Programmer(Employee):
    company = "Google1"
    def showLanguage(self):
        print(f"the programmer{self.name} is fluent in {self.language}")
        
a = Employee()
b = Programmer()

print(a.company, b.company)

a.name = "Animesh"
a.language = 123456

print(a.name, a.language)


