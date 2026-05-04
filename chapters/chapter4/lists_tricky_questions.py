# 🔹 Q1
lst = [1, 2, 3]
# * 2 duplicates elements, not references
# Works like concatenation
print(lst * 2) #[1,2,3,1,2,3]

# 🔹 Q2
lst = [1, 2, 3]
# Deep Insight ⚠️
# This creates two references to the SAME list
# Not two separate lists

# 👉 Memory:

# [ lst_ref, lst_ref ]
print([lst] * 2) #[[1,2,3],[1,2,3]]

# 🔹 Q3
a = lst
a.append(4)
# a = lst → both point to same memory
# No copy is made
print(lst) #why? [1, 2, 3, 4] because when we assign 'a' to 'lst', both 'a' and 'lst' reference the same list object in memory. Therefore, when we append 4 to 'a', it modifies the same list that 'lst' references, resulting in the original list being modified to [1, 2, 3, 4]. 

# 🔹 Q4
a = lst.copy()
a.append(5)
print(lst) #why? [1, 2, 3, 4] : because copy() creates a shallow copy of the list, which means that it creates a new list object but does not create new objects for the items in the list. Therefore, when we modify the list 'a', it does not modify the original list 'lst' since they are two different list objects.

# 🔹 Q5
lst = [[1, 2], [3, 4]]
a = lst.copy()
a[0][0] = 99
# Why (Shallow Copy Trap)
# Outer list is copied
# Inner lists are shared references

# 👉 Memory:

# lst --> [ref1, ref2]
# a   --> [ref1, ref2]
print(lst) #why? [[99, 2], [3, 4]] because copy() creates a shallow copy of the list, which means that it creates a new list object but does not create new objects for the items in the list. Therefore, when we modify the nested list in 'a', it also modifies the nested list in 'lst' since they both reference the same nested list object.

# 🔹 Q6
lst = [1, 2, 3]
print(lst[::-1]) #why? [3, 2, 1] because slicing with a step of -1 creates a new list that is a reversed version of the original list. The original list 'lst' remains unchanged, and the new list is printed in reverse order.

# 🔹 Q7
lst = [1, 2, 3, 4, 5]
print(lst[1:4]) #why? [2, 3, 4] because slicing with [1:4] creates a new list that includes the items from index 1 to index 3 (the end index is exclusive). Therefore, it includes the items at indices 1, 2, and 3, which are 2, 3, and 4 respectively. The original list 'lst' remains unchanged. 

# 🔹 Q8
lst = [1, 2, 3]
lst.append([4, 5])
print(len(lst)) #4 as we are not extending we are appending

# 🔹 Q9
lst = [1, 2, 3]
lst.extend([4, 5])
print(lst, len(lst))

# 🔹 Q10
lst = [10, 20, 30]
print(lst.pop(1)) #why? 20 because pop() method removes and returns the item at the specified index. In this case, it removes and returns the item at index 1, which is 20. After this operation, the list 'lst' will be modified to [10, 30].
print(lst) #why? [10, 30] because after the pop() method is called, the item at index 1 (which is 20) is removed from the list 'lst'. Therefore, the modified list 'lst' will contain only the remaining items, which are 10 and 30.

# 🔹 Q11
lst = [10, 20, 30]
print(lst.remove(20)) #why? None because remove() method removes the first occurrence of the specified value from the list. In this case, it removes the value 20 from the list 'lst'. However, the remove() method does not return any value, so it returns None. After this operation, the list 'lst' will be modified to [10, 30].

# 🔹 Q12
lst = [2, 3,1,4]
print(sorted(lst)) #why? [1, 2, 3, 4] because sorted() function returns a new sorted list from the items in the iterable. In this case, it takes the list 'lst' and returns a new list that is sorted in ascending order. The original list 'lst' remains unchanged.
print(lst)

# 🔹 Q13
lst = [[]] * 3
lst[0].append(1)
# Why?
# Same list repeated 3 times

# 👉 Memory:

# [ref, ref, ref]
print(lst) #why? [[1], [1], [1]] because when we create a list using the multiplication operator, it creates multiple references to the same inner list. Therefore, when we append 1 to the first inner list (lst[0]), it also modifies the other two inner lists since they reference the same list object. As a result, all three inner lists contain the value 1, resulting in [[1], [1], [1]].

# 🔹 Q14
lst = [1, 2, 3]
print(id(lst)) #why? The id() function returns the identity of an object, which is a unique integer that remains constant for the object during its lifetime. In this case, it will return the memory address of the list 'lst'. The specific value returned by id() will vary each time you run the program, as it depends on where the list is stored in memory.
lst = lst + [4]
print(id(lst))

# FINAL INTERVIEW SUMMARY
# ⚡ Must Remember:
# = → reference
# .copy() → shallow copy
# Nested lists → still shared ⚠️
# append() vs extend() → BIG difference
# In-place methods → return None
# + → new object
# * → duplicates references sometimes