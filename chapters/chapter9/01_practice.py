class Programmer:
  company = "Micorsoft"
  def __init__(self, name, designation, salary):
    self.name = name
    self.designation = designation
    self.salary = salary
  def getDetails(self):
    print(f'Name is {self.name}. Deisgnation is {self.designation}. And salry is {self.salary}')

shikha = Programmer('Shikha', "Senior Software engineer", "15000")
print(shikha.company)
shikha.getDetails()