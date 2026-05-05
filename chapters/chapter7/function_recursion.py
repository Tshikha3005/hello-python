# def func(name, ending="Thank you"):
#   print(f"Good Day, {name}!!")
#   print(ending)
# func("Shikha")

# recursion
# fact
def fact(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact(n-1)

print(fact(5))