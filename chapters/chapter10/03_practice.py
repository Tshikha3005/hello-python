class Employee:
  @property
  def salaryInc(self):
    return (self.salary + self.salary * (self.inc/100))
  
  @salaryInc.setter
  def salaryInc(self,salary):
    self.inc = ((salary/self.salary) - 1)* 100
# inc = 
emp = Employee()
emp.salary = 234
emp.inc = 20
emp.salaryInc = 400
print(emp.inc)