from functools import reduce

l = ['apple','mango','banana']

final = "::".join(l)

print(final) #apple::mango::banana

a = "{} is a good {}".format("shikha", "girl")
print(a)

# MAP
# map(function, input_list)
l = [1,2,3,4,5]
squareList = list(map(lambda x:x*x, l))
print(squareList)

filterList = list(filter(lambda x:x%2 == 0, l))
print(filterList)

def sum(a,b):
  return a + b
sumList = reduce(sum, l)
print(sumList)