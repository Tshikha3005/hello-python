# Tuple is an immutable sequence type, which means that once a tuple is created, its contents cannot be changed.
# Tuples are defined by enclosing a comma-separated sequence of items in parentheses. For example: (1, 2, 3)
# Tuples can be indexed and sliced just like lists. The first item in a tuple has index 0, the second item has index 1, and so on. The last item in a tuple can be accessed using the index -1, the second to last item can be accessed using the index -2, and so on.
# Tuples can be nested, which means that you can have a tuple that contains other tuples as its items. For example: ((1, 2), (3, 4), (5, 6))
# Tuples have a number of built-in methods that allow you to manipulate them. For example, you can use the count() method to count the number of occurrences of an item in a tuple, and the index() method to find the index of the first occurrence of an item in a tuple.
# Here are some examples of how to use tuples in Python:
# Create a tuple of integers
my_tuple = (1, 2, 3)
# Access items in the tuple
my_tuple[0]  # 1
print(my_tuple[1])  # 2

# my_tuple[0] = 10  # This will raise a TypeError because tuples are immutable and cannot be modified after they have been created.
# print(my_tuple)  # Output: (1, 2, 3)

a = (1)
print(a)  # Output: 1
b = (1,) 
print(b)  # Output: (1,) because when you create a tuple with a single item, you need to include a comma after the item to indicate that it is a tuple. If you omit the comma, Python will interpret it as an integer instead of a tuple. Therefore, 'a' is an integer with the value 1, while 'b' is a tuple containing the single item 1.

a = (1,2,3, 1)
print(a.index(1))  # Output: 0 because the index() method returns the index of the first occurrence of the specified value in the tuple. In this case, the first occurrence of the value 1 is at index 0, so it returns 0.
print(a.count(1))  # Output: 2 because the count() method returns the number of occurrences of the specified value in the tuple. In this case, the value 1 appears twice in the tuple, so it returns 2.

print(type(a)) # Output: <class 'tuple'> because 'a' is defined as a tuple using parentheses, so its type is <class 'tuple'>.

# 🔑 Key Properties
# 1. ✅ Ordered
# Index-based access
# t[0]  # 1
# 2. ❌ Immutable (MOST IMPORTANT)

# 👉 You cannot change elements

# t[0] = 10   # ❌ Error
# 3. ✅ Allows duplicates
(1, 2, 2, 3)
# 4. ✅ Can store mixed data types
(1, "hello", True)

t2= 1,2,3
print(t2) # Output: (1, 2, 3) because when you create a tuple without using parentheses, Python will still interpret it as a tuple as long as there are multiple items separated by commas. Therefore, 't2' is a tuple containing the items 1, 2, and 3, and it will be printed in the format of a tuple with parentheses.

# packing and unpacking

