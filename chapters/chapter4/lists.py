# Lists: A list ca nbe indexed just like a string
# lists are containers that hold a number of items. The items can be of any type, and they can be of different types within the same list. Lists are mutable, which means that you can change their contents after they have been created.
# Lists are defined by enclosing a comma-separated sequence of items in square brackets. For example:['spam', 'eggs', 'toast', 'bread']
# Lists can be indexed and sliced just like strings. The first item in a list has index 0, the second item has index 1, and so on. The last item in a list can be accessed using the index -1, the second to last item can be accessed using the index -2, and so on.
# Lists can be nested, which means that you can have a list that contains other lists as its items. For example: [['cat', 'dog', 'mouse'], [1, 2, 3], ['a', 'b', 'c']]
# Lists have a number of built-in methods that allow you to manipulate them. For example, you can use the append() method to add an item to the end of a list, the insert() method to add an item at a specific index, and the remove() method to remove an item from a list.
# Here are some examples of how to use lists in Python:
# Create a list of strings
my_list = ['spam', 'eggs', 'toast', 'bread']
# Access items in the list
my_list[0]  # 'spam'
my_list[1]  # 'eggs'
my_list[-1]  # 'bread'
# Create a nested list
nested_list = [['cat', 'dog', 'mouse'], [1, 2, 3], ['a', 'b', 'c']]
# Access items in the nested list
nested_list[0]  # ['cat', 'dog', 'mouse'] 
nested_list[1]  # [1, 2, 3]

# Manipulate lists
# append() method adds an item to the end of the list 
my_list.append('ham')  # my_list is now ['spam', 'eggs', 'toast', 'bread', 'ham']
# extend() method adds all the items in a list to the end of another list
my_list.extend(['bacon', 'sausage'])  # my_list is now ['spam', 'eggs', 'toast', 'bread', 'ham', 'bacon', 'sausage']
# insert() method adds an item at a specific index
my_list.insert(1, 'bacon')  # my_list is now ['spam', 'bacon', 'eggs', 'toast', 'bread', 'ham']
# remove() method removes an item from the list
my_list.remove('toast')  # my_list is now ['spam', 'bacon', 'eggs', 'bread', 'ham'] 
# pop() method removes and returns the last item in the list
last_item = my_list.pop()  # last_item is 'ham' and my_list is now ['spam', 'bacon', 'eggs', 'bread']
print(last_item)  # Output: 'ham'
# clear() method removes all the items from the list
my_list.clear()  # my_list is now []
# index() method returns the index of the first occurrence of an item in the list
my_list = ['spam', 'eggs', 'toast', 'bread']
index_of_eggs = my_list.index('eggs')  # index_of_eggs is 1
print(index_of_eggs)  # Output: 1
# count() method returns the number of occurrences of an item in the list
count_of_bacon = my_list.count('bacon')  # count_of_bacon is 0
print(count_of_bacon)  # Output: 0
# sort() method sorts the items in the list
my_list.sort()  # my_list is now ['bacon', 'bread', 'eggs', 'spam']
# reverse() method reverses the order of the items in the list
my_list.reverse()  # my_list is now ['spam', 'eggs', 'bread', 'bacon']
my_list[0] = 'sausage'  # my_list is now ['sausage', 'eggs', 'bread', 'bacon']
my_list[0] = 'hotdog'  # my_list is now ['hotdog', 'eggs', 'bread', 'bacon']
my_list[1:3] = ['ham', 'toast']  # my_list is now ['hotdog', 'ham', 'toast', 'bacon'] change kr diya hai
# copy() method creates a shallow copy of the list  
my_list_copy = my_list.copy()  # my_list_copy is ['hotdog', 'ham', 'toast', 'bacon']
print(my_list_copy)  # Output: ['hotdog', 'ham', 'toast', 'bacon']


# Important 
# ⚠️ append() vs extend()
lst = [1, 2]
lst.append([3, 4])   # [1, 2, [3, 4]]
lst.extend([3, 4])   # [1, 2, 3, 4]

# sort() vs sorted()
lst = [3, 1, 2]

lst.sort()        # modifies original
sorted(lst)       # returns new list