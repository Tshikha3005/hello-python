# “A tuple is an ordered, immutable collection in Python that allows duplicates and is commonly used for fixed data and as dictionary keys.”
# Tricky Concept (VERY IMPORTANT)
# ❗ Tuple is immutable BUT:
t = ([1, 2], [3, 4])
t[0].append(99)
print(t)
# ✅ Output:
# ([1, 2, 99], [3, 4])
# 🧠 Why?
# Tuple is immutable ❌
# But elements inside can be mutable ✅

# 🔥 Why Use Tuples?
# ✅ 1. Faster than lists
# ✅ 2. Safe (cannot change accidentally)
# ✅ 3. Used as dictionary keys
d = {(1, 2): "value"}   # ✅ valid
# ❌ Why list cannot be key?
# d = {[1, 2]: "value"}   # ❌ Error

# 👉 Because lists are mutable

# 🧠 Real Use Cases
# Coordinates: (x, y)
# Database records
# Returning multiple values from functions
def get_user():
    return ("Shikha", 25)

print(get_user())  # Output: ('Shikha', 25) because the function get_user() returns a tuple containing the name "Shikha" and the age 25. When we call the function, it returns the tuple, which is printed in the format of a tuple with parentheses.  

# SECTION 1: Basic Tuple Traps
# 🔹 Q1
t = (1)
print(t)  # Output: 1 because when you create a tuple with a single item, you need to include a comma after the item to indicate that it is a tuple. If you omit the comma, Python will interpret it as an integer instead of a tuple. Therefore, 't' is an integer with the value 1, and it will be printed as 1 without parentheses.

# 🔹 Q2
t = (1,)
print(t)  # Output: (1,) because when you create a tuple with a single item, you need to include a comma after the item to indicate that it is a tuple. Therefore, 't' is a tuple containing the single item 1, and it will be printed in the format of a tuple with parentheses.

# 🔹 Q3
t = 1,2,3
print(t) # Output: (1, 2, 3) because when you create a tuple without using parentheses, Python will still interpret it as a tuple as long as there are multiple items separated by commas. Therefore, 't' is a tuple containing the items 1, 2, and 3, and it will be printed in the format of a tuple with parentheses.

# 🔹 Q4
t= (1,2,3)
print(t[1]) # Output: 2 because tuples are ordered and indexed, so you can access individual elements using their index. In this case, t[1] refers to the second element of the tuple, which is 2, and it will be printed as 2 without parentheses.

# 🔹 Q5
t = (1, 2, 3)
# t[0] = 10 throw error because tuples are immutable, which means that once a tuple is created, its contents cannot be changed. Therefore, trying to assign a new value to an element of the tuple will result in a TypeError. In this case, t[0] = 10 will raise a TypeError because it attempts to modify the first element of the tuple, which is not allowed.

# Immutability Traps
# 🔹 Q6
t = ([1, 2], [3, 4])
t[0].append(99)
print(t) # Output: ([1, 2, 99], [3, 4]) because while the tuple itself is immutable and cannot be modified, the elements inside the tuple can be mutable. In this case, the first element of the tuple is a list [1, 2], which is mutable. When we call the append() method on that list, it modifies the list in place, resulting in the updated list [1, 2, 99]. The second element of the tuple remains unchanged as [3, 4]. Therefore, when we print the tuple 't', it shows the modified first element and the unchanged second element.

# 🔹 Q7
# t(1,2,[3,4])
# t[2] = [5,6]
# print(t) # Output: TypeError because tuples are immutable, which means that once a tuple is created, its contents cannot be changed. Therefore, trying to assign a new value to an element of the tuple will result in a TypeError. In this case, t[2] = [5,6] will raise a TypeError because it attempts to modify the third element of the tuple, which is not allowed.

# 🔹 Q8
t = (1, 2, 3)
print(id(t))
t = t + (4,)
print(id(t)) # Output: different memory addresses because when we concatenate a new tuple (4,) to the existing tuple 't', it creates a new tuple object in memory. Therefore, the memory address of the original tuple 't' will be different from the memory address of the new tuple that is created after concatenation. When we print the memory addresses using id(t), we will see that they are different, indicating that a new tuple object has been created.

# packing and unpacking traps
# 🔹 Q9
a = 1,2,3
x,y,z = a
print(x,y,z) # Output: 1 2 3 because when we assign the tuple 'a' to the variables x, y, and z, it unpacks the values from the tuple and assigns them to the respective variables. Therefore, x will be assigned the value 1, y will be assigned the value 2, and z will be assigned the value 3. When we print x, y, and z, it will output 1 2 3 as they hold the values from the tuple 'a'.

# 🔹 Q10
a = (1,2,3)
# x,y = a # Output: ValueError because when we try to unpack the tuple 'a' into the variables x and y, it expects exactly 2 values to unpack. However, the tuple 'a' contains 3 values (1, 2, and 3), which cannot be unpacked into just 2 variables. Therefore, it will raise a ValueError indicating that there are too many values to unpack.

# 🔹 Q11
a =(1,2,3)
x, *y = a
print(x, y) #x= 1, y = [2,3] because when we unpack the tuple 'a' using the syntax x, *y, it assigns the first value of the tuple (1) to the variable x, and the remaining values (2 and 3) are collected into a list and assigned to the variable y. Therefore, x will be 1, and y will be a list containing [2, 3]. When we print x and y, it will output 1 [2, 3].

# 🔹 Q12
a = (1, 2, 3, 4, 5)
x, *y, z = a
print(x, y, z)

# x = 1, y = [2, 3, 4], z = 5 because when we unpack the tuple 'a' using the syntax x, *y, z, it assigns the first value of the tuple (1) to the variable x, the last value of the tuple (5) to the variable z, and the remaining values (2, 3, and 4) are collected into a list and assigned to the variable y. Therefore, x will be 1, y will be a list containing [2, 3, 4], and z will be 5. When we print x, y, and z, it will output 1 [2, 3, 4] 5.

# 🔹 Q13
t = (1, (2,3),4)
a, (b,c),d = t
print(a,b,c,d) # Output: 1 2 3 4 because when we unpack the tuple 't' using the syntax a, (b, c), d, it assigns the first value of the tuple (1) to the variable a, the second value (which is a nested tuple (2, 3)) is unpacked into variables b and c, and the last value (4) is assigned to the variable d. Therefore, a will be 1, b will be 2, c will be 3, and d will be 4. When we print a, b, c, and d, it will output 1 2 3 4.

# 🔹 Q14
t = (1, (2, 3), 4)
a, b, c = t
print(a, b, c) # Output: 1 (2, 3) 4 because when we unpack the tuple 't' using the syntax a, b, c, it assigns the first value of the tuple (1) to the variable a, the second value (which is a nested tuple (2, 3)) is assigned to the variable b as a whole, and the last value (4) is assigned to the variable c. Therefore, a will be 1, b will be the tuple (2, 3), and c will be 4. When we print a, b, and c, it will output 1 (2, 3) 4.

# 🔹 Q15
t = (1, (2, 3), 4)
# a,b,c,d = t
# print(a,b,c
# ,d) # Output: ValueError because when we try to unpack the tuple 't' into the variables a, b, c, and d, it expects exactly 4 values to unpack. However, the tuple 't' contains only 3 values (1, (2, 3), and 4), which cannot be unpacked into 4 variables. Therefore, it will raise a ValueError indicating that there are not enough values to unpack.

# 🔹 Q16
t = (1, (2, 3), 4)
# a, (b, c, d), e = t
# print(a,b,c,d,e) # Output: ValueError because when we try to unpack the tuple 't' using the syntax a, (b, c, d), e, it expects the second element of the tuple (which is (2, 3)) to contain exactly 3 values to unpack into variables b, c, and d. However, the second element of the tuple only contains 2 values (2 and 3), which cannot be unpacked into 3 variables. Therefore, it will raise a ValueError indicating that there are not enough values to unpack in the nested tuple.

# 🔹 Q17
t = ((1, 2), (3, 4))
(a,b), (c,d) = t
print(a,b,c,d) # Output: 1 2 3 4 because when we unpack the tuple 't' using the syntax (a, b), (c, d), it assigns the first nested tuple (1, 2) to the variables a and b, and the second nested tuple (3, 4) to the variables c and d. Therefore, a will be 1, b will be 2, c will be 3, and d will be 4. When we print a, b, c, and d, it will output 1 2 3 4.

# 🔹 Q18
a= 10
b= 20
a, b = b, a
print(a,b) # Output: 20 10 because when we use the syntax a, b = b, a, it performs a simultaneous assignment where the value of b (which is 20) is assigned to a, and the value of a (which is 10) is assigned to b. Therefore, after this operation, a will be 20 and b will be 10. When we print a and b, it will output 20 10. This technique is commonly used for swapping values without needing a temporary variable.

# 🔹 Q19
def func():
    return 1, 2, 3

a = func()
print(a) # Output: (1, 2, 3) because the function func() returns a tuple containing the values 1, 2, and 3. When we call the function and assign its return value to the variable 'a', it will hold the tuple (1, 2, 3). When we print 'a', it will output (1, 2, 3) in the format of a tuple with parentheses.
print(type(a)) # Output: <class 'tuple'> because the function func() returns a tuple, and when we assign that return value to the variable 'a', it becomes a tuple. Therefore, when we check the type of 'a' using type(a), it will return <class 'tuple'>, indicating that 'a' is indeed a tuple.

# 🔹 Q20
def func():
    return 1, 2, 3

x, y, z = func()
print(x,y,z) # Output: 1 2 3 because the function func() returns a tuple containing the values 1, 2, and 3. When we unpack the return value of the function into the variables x, y, and z using the syntax x, y, z = func(), it assigns the first value of the tuple (1) to x, the second value (2) to y, and the third value (3) to z. Therefore, x will be 1, y will be 2, and z will be 3. When we print x, y, and z, it will output 1 2 3.

# 🔹 Q21
a = (1,2,3)
print(a * 2) # Output: (1, 2, 3, 1, 2, 3) because when we multiply a tuple by an integer, it creates a new tuple that repeats the original tuple the specified number of times. In this case, a * 2 creates a new tuple that contains the elements of 'a' repeated twice. Therefore, the resulting tuple will be (1, 2, 3, 1, 2, 3), which is printed as the output.

# 🔹 Q22
a = ([1],[2])
b = a
b[0].append(99)
print(a) # Output: ([1, 99], [2]) because when we assign 'a' to 'b', both 'a' and 'b' reference the same list object in memory. Therefore, when we modify the first element of the list (which is [1]) by appending 99 to it, it modifies the list that both 'a' and 'b' reference. As a result, when we print 'a', it shows the modified list with 99 appended to the first element, resulting in ([1, 99], [2]).

# 🔹 Q23
a = ([1], [2])
b = a.copy() if hasattr(a, "copy") else a
b[0].append(99)
print(a) # Output: ([1, 99], [2]) because the copy() method creates a shallow copy of the list 'a', which means that it creates a new list object but does not create new objects for the items in the list. Therefore, when we modify the first element of the list 'b' (which is [1]) by appending 99 to it, it also modifies the first element of the list 'a' since both 'a' and 'b' reference the same inner list object. As a result, when we print 'a', it shows the modified list with 99 appended to the first element, resulting in ([1, 99], [2]).

# 🔹 Q24
print((1,2) < (1,3)) # Output: True because when we compare two tuples, Python compares them element by element. In this case, it first compares the first elements of the tuples (1 and 1), which are equal. Then it compares the second elements (2 and 3). Since 2 is less than 3, the comparison (1, 2) < (1, 3) evaluates to True.

# 🔹 Q25
lst = [(1,3),(1,2),(2,1)]
lst.sort()
print(lst) # Output: [(1, 2), (1, 3), (2, 1)] because when we sort a list of tuples, Python sorts them based on the first element of each tuple. If there are ties in the first element, it then sorts based on the second element, and so on. In this case, the tuples are sorted first by the first element (1 and 2), and for the tuples with the same first element (1), they are sorted by the second element (2 and 3). Therefore, the sorted list will be [(1, 2), (1, 3), (2, 1)].