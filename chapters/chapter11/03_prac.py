try:
  a = int(input("Enter vaqlue of a: "))
  b = int(input("Enter vaqlue of b: "))
  print(a/b)
except ZeroDivisionError as v:
  print("Infinte")
