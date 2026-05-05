# reverse star

def reverse(n):
  if n == 0:
    return 
  print("*"*n, end='')
  print("")
  reverse(n-1)

reverse(3)