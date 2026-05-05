
class Calculator:
  def __init__(self, n):
    self.n = n

  def square(self):
    print(self.n * self.n)

  def cube(self):
    print(self.n * self.n * self.n)
  
  def squareRoot(self):
    print(self.n**1/2)

  @staticmethod
  def greet():
    print("Hello, how are you?")
a = Calculator(4)
a.square()
a.cube()
a.squareRoot()
a.greet()