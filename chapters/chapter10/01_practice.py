class TwoDVector:
  def __init__(self,a,b):
    self.a = a
    self.b = b

class ThreeDVector(TwoDVector):
  def __init__(self, a, b, c):
    super().__init__(a, b)
    self.c = c
    print(a,b,c)

c_2= TwoDVector(1,2)
c_3= ThreeDVector(5,23,3)

c_3.a
c_3.b
c_3.c