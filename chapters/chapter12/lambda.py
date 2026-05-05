def square(n):
  return n * n

print(square(5))

# Lambda Functions: Functions creates an expresiion using lambda keyword
# lambda arguments:expressions

square = lambda x:x*x
print(square(6))

sum = lambda a,b,c: a+b+c
print(sum(1,2,3))

# Python Anonymous Function- LAMBDA
# It is a function defined without a name.
# 	Lambda arguments : expression
# In python we generally use it as an argument to a higher order function

# Filter()- takes ina function and a list as arguments.
my_list=[1,5,4,6,8,11,3,2]
new_list=list(filter(lambda x:(x%2==0), my_list))
print (new_list)

# map()- takes in a function and a list. A function is called with all the elements in the list. 
# And a new list is returned which contains items returned by that function for each item
my_list=[1,5,4,6,8,11,3,2]
new_list=list(map(lambda x:x*2, my_list))
print (new_list)
