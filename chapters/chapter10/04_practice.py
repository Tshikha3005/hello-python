class Complex:
  def __init__(self, r, t):
    self.r = r
    self.t = t

  def __add__(self, c2):
    return Complex(self.r + c2.r, self.t + c2.t)

  def __mul__(self, other):
    return Complex(self.r * other.r, self.t * other.t)

  def __str__(self):
    return f"{self.r} + {self.t}"
c1 = Complex(1,2)
c2 = Complex(3,4)
print(c1 + c2)
print(c1 * c2)