# @property decorators
class Employee:
  a = 1
  @classmethod
  def show(cls):
    print(f"The class value of a is {cls.a}")
# The @property Decorator (The Getter)
# This decorator tells Python that a method should be accessed like an attribute. 
# Instead of calling obj.name(), you can just type obj.name.

# Purpose: To "get" or "read" a value.

# Benefit: You can calculate a value on the fly (like combining a first and last name) without storing it as a separate variable.
  @property
  def name(self):
    return f"{self.fname} {self.lname}"
  
#   The @name.setter Decorator (The Setter)
# This allows you to change the value of that property using the assignment operator (=).

# Purpose: To "set" or "write" a value.

# Benefit: You can add validation. For example, you can check if a score is between 0 and 100 before actually saving it.
  @name.setter
  def name(self, value):
    self.fname = value.split(' ')[0]
    self.lname = value.split(' ')[1]
  
e = Employee()
e.a = 45

e.name = 'Shikha Thakur'
print(e.name)
print(e.show(), e.fname, e.lname)

# This is abstraction and encapsulation