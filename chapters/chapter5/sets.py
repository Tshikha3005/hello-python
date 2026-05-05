# Unordered collection of unique elements
# unindexed => cannot access elements by Index
# no way to change itsms in sets

s = {1,2,3}

# ⚡ Key Properties
# ❌ No duplicates
# ❌ No indexing
# ❌ Unordered
# ✅ Fast lookups (O(1))
#  to create empty set 
f = set()
print(f)
s.add(4)
s.remove(2) #errori if not found
s.discard(5) #its safe it will not thorw error
s.pop() #remove an arbitrary element from the set and return the element removed
s.union({8,11}) #return new element with all the items from both the set
s.intersection({8,11}) #8 as only 8 is common
s.clear()
print(s)

# Sets Operations
a = {1,2,3}
b={3,4,5}

a | b #union => {1,2,3,4,5}
a & b #intersection => {3}
a - b #diff => {1,2}
a ^ b #symmetirc diff => {1,2,4,5}

# 🧠 Use Cases
# Remove duplicates
# Membership check (fast)
# DSA problems (intersection, uniqueness)