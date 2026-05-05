# # __init__() constructor
# class Employee:
#   language = "JS"
#   salary = 1200000
#   def __init__(self): # this is a dunder methos which is automatically called. It starts with __. it will automatically called.
#     print("I am creatig an object")
# # We did nt cal init function still getting this printed, why??
# # this is a special method this is a
# shikha = Employee()
# shikha.name = 'Shikha'
# print(shikha.name, shikha.salary, shikha.language)

class Employee:
  def __init__(self, name, salary, language):
    self.name = name
    self.salary = salary
    self.language = language
    print("I am acreated")

shikha = Employee("Shikha", 1500000, "JS")

print(shikha.name, shikha.language, shikha.salary)