class Employee:
    company = "Google"
    def show(self):
        print(f"the name is{self.company} and salary is 200000")
        
class Coder:
    language = "Python"
    def peintLanguage(self):
        print(f"the coder is fluent in {self.language}")
        
class Programmer(Employee, Coder):
    company = "Google1"
    language = "C++"
    def showLanguage(self):
        print(f"the programmer is fluent in {self.language}")
        
a = Employee()
b = Programmer()

print(a.company, b.company)

a.name = "Animesh"
a.language = 123456

b.peintLanguage()




