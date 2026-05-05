l = [1,5,12,15,10,25,20,45,32,23,43,76]
print(list(filter(lambda n:n%5==0, l)))
print([1,2]*2)
# In Python, logical operators don't just return True or False; they return the actual value of one of the operands.
# Truthy vs Falsy: In Python, 0, None, and empty containers ([], {}) are considered Falsy. Almost everything else (like numbers 5 or 234) is Truthy.
# Python stops evaluating as soon as it knows the final result.
# The and operator looks for the first Falsy value. If it finds one, it returns it immediately. If all values are Truthy, it returns the last value.
print( 0 and 5) # 0
print(234 and 5) # 5
print(234 and 5 and 0) # 0
# The or operator looks for the first Truthy value. If it finds one, it returns it immediately. If all values are Falsy, it returns the last value.
print(0 or 5) # 5
print(234 or 5) # 234
print(234 or 5 or 0) # 234