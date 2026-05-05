class Animals:
  def __init__(self):
    print('These lives in wild')

class Pets(Animals):
  def __init__(self):
    super().__init__()
    print("These liveds in houses with humans")

class Dog(Pets):
  def __init__(self):
    super().__init__()
  def bark(self):
    return "Dog barks a lot"
  
ani = Animals()
Pet = Pets()
do = Dog()

do.bark()