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

class Manager(Programmer):
  def selectLead(self):
    print(f'{self.name} is experienced in {self.language} and has good exposeure of {self.company} so i think she should get {self.salary}')

a = Employee()
b = Programmer()
c = Manager()

b.show()
b.showLanguage()
b.printLanguage()
c.selectLead()