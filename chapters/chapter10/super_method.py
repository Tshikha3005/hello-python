# super().__init__
# calls constructor of the base class
#  this is used to access methods of the super class in derived class

class Parent:
  def __init__(self):
    self.name = "Parent"

class Child(Parent):
  def __init__(self):
#     👉 You overrode __init__

# 👉 Result:
# Parent __init__ ❌ NOT called
# Child __init__ ✅ called
    self.age = 25

# a = Parent()
# b = Child()

# print(a.name, b.name,b.age) #Error :AttributeError: 'Child' object has no attribute 'name'

# To correct this we need to do super()._init__() this will call Parent
class ChildB(Parent):
  def __init__(self):
    super().__init__()
    self.age = 25

a = Parent()
b = ChildB()

print(a.name, b.name,b.age) #Error :AttributeError: 'Child' object has no attribute 'name'

# Correct flow
# Child.__init__()
#     ↓
# super().__init__()
#     ↓
# Parent.__init__()
#     ↓
# name set
# When a child class defines its own constructor, the parent constructor is not automatically invoked, so we use super() to explicitly call it.
# Inheritance gives access — super() lets you CONTROL how parent code runs.
# Concept	Meaning
# Inheritance	“I can access parent”
# super()	“I choose to run parent logic”
# When should YOU use super()?
# ✅ Use it when:
# You override __init__
# You extend parent method
# Multiple inheritance involved
