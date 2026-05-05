# multiplication in reverse order

n = int(input("Enter no for multiplication: "))

for i in range(10,0,-1):
  print(n, '*', i,'=',n* i)

for i in range(1,11):
  print(f"{n} X {11-i} = {n*(11-i)}")