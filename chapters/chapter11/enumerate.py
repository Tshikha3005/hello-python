l = [3,513,53,535]
for index,item in enumerate(l): #will work for list
  print(index,item)

# list comprehension
myList = [1,2,5,3,5,9]
squareList = []

# for item in myList:
#   squareList.append(item*item)
# List comprehensions provide a concise way to create lists in Python. Instead of using a for loop and the .append() method to build a list, you can do it in a single line.
squareList=[i*i for i in myList]
# new_list = [item for item in iterable if condition]
newList = [i*i for i in myList if i%2 == 0]
print(squareList, newList)
