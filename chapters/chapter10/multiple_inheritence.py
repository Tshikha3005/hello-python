class Employee:
  company = 'ITC'
  name = 'Shikha'
  salary = '34234234'
  def show(self):
    print(f"The name is {self.name} and the salary is {self.salary}")

class Coder:
  language = 'Python'
  def printLanguage(self):
    print(f"She is experienced in {self.language}")

class Programmer(Employee, Coder):
  company = 'ITC Infotech'
  def showLanguage(self):
    print(f"The name is {self.name} and he is good in {self.language}")

a = Employee()
b = Programmer()

b.show()
b.showLanguage()
b.printLanguage()