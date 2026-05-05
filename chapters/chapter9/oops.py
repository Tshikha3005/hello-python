# Object oriented programming

# Solve a project by creating object is one of the most popular approaches in the programming.
# Concept based on reusuable code (DRY Principle)

# Class is a blue print of object
# Class name i s written in PAscal case
# an object is an instantiation of a class. When class is defined a template is defined. Memory is allocated only after object initiation
# object of a class can invoke the methods available without revealing the implementation detailted to the user.
# Note: those are encalpsulation and Absttraction
class Employee:
  name = 'Shikha' #this is class attribute
  language = 'JS'
  salary = 1200000
  def details(self):
    print(f'{self.name} {self.language} {self.salary}') # this is wrong
  @staticmethod
  def greet(): # here did get the type error becuse we have mentioned static method. it says it doesnt need object
    print("Good morning")
shikha = Employee() #object initiation
shikha.name = "Shikha thakur" #this is instance attribute
shikha.details() #Employee.details(shikha) it is converting to this so that. why gettign error TypeError: Employee.details() takes 0 positional arguments but 1 was given
# instance attribute takes precedence over class attributes during assignment and retrieval.
mradul = Employee()
shikha.greet() 
# static method
