# A class method is a  method which is bound to the class and not the object of the class.
# @classmethod decorator is used to create a class method
# method ke andr directly class ko acces krne ka
class Employee:
  a = 1
  def show(self):
    print(f"The class value of a is {self.a}")

e = Employee()
e.a = 45 #instance attribute

e.show()

# but we want class attirbute so we need do class method

class Employee:
  a = 1
  @classmethod
  def show(cls):
    print(f"The class value of a is {cls.a}")

e = Employee()
e.a = 45 #instance attribute

e.show() #now it will show 1 class atribute

# decorators.py

# """decorators- special functions tht return other functions.
# used to modify the way a function works.
# can fundamentally change behaviour of a function.
# """
# """
# for example- if we want to save it to a db or if we want to create a db based on a filename.
# """

class Duck:
#     1. Flexible Initialization (kwargs)
# Instead of defining specific variables like self.color or self.name, you use kwargs.

# This allows you to pass any number of keyword arguments when creating a duck (e.g., Duck(color='red', age=2)).

# All these are stored in a single dictionary called self.properties.
    def __init__(self, **kwargs):
        self.properties = kwargs
        
    def talk(self):
        print("quack")

    def walk(self):
        print ("walk i a duck")

    def get_properties(self):
        return self.properties

    def get_property(self,key):
        return self.properties.get(key, None)

# The @property Decorator (The Getter)
# The @property decorator turns a method into a "read-only" attribute.

# Effect: You can access the color by typing du.color instead of du.color().

# Benefit: It allows you to add logic (like validation) later without changing how the rest of your code accesses the data.
    @property
    def color(self):
        return self.properties.get('color', None)

# The .setter Decorator
# This allows you to "assign" a value to a method as if it were a variable.

# When you write du.color = 'blue' in your main() function, Python actually calls the def color(self, c): method behind the scenes and updates the dictionary.
    @color.setter
    def color(self,c):
        self.properties['color'] = c

# The .deleter Decorator
# This defines what happens if someone types del du.color. Currently, yours returns the value but doesn't actually delete it from the dictionary (to fix this, you would use del self.properties['color']).
    @color.deleter
    def color(self):
        return self.properties['color']
        


def main():
    du = Duck()
    du.color='blue'
    print(du.get_property('color'))
    print(du.get_properties())

if __name__== "__main__": main()    