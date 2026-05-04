# 🧠 1. What is Packing?

# 👉 Packing = putting multiple values into one variable (tuple)

t = 1, 2, 3

# 👉 Python automatically does:

t = (1, 2, 3)
# 💡 Think like:

# “Pack these values into one box”

# 📦

t = (1, 2, 3)
# 🧠 2. What is Unpacking?

# 👉 Unpacking = taking values out of that box into variables

t = (1, 2, 3)

a, b, c = t
# ✅ Result:
# a = 1
# b = 2
# c = 3
# 💡 Think like:

# 📦 (1, 2, 3) → 🎁 → a, b, c

# 🔥 MOST IMPORTANT RULE

# 👉 Number of variables = number of values

# a, b = (1, 2, 3)   # ❌ Error
# 🧠 3. Why is this useful?
# Example:
def get_user():
    return "Shikha", 25   # packing

name, age = get_user()   # unpacking
# 🔥 4. Advanced Unpacking (⭐ VERY IMPORTANT)
a, *b = (1, 2, 3, 4)
# ✅ Result:
# a = 1
# b = [2, 3, 4]

# 👉 * collects remaining values

# More Examples:
*a, b = (1, 2, 3, 4)
a = [1, 2, 3]
b = 4
a, *b, c = (1, 2, 3, 4, 5)
a = 1
b = [2, 3, 4]
c = 5
# 💀 Common Mistake
# a, b, c = (1, 2)   # ❌ not enough values
# 🔥 Real Interview Trick
# Swap without temp variable
a = 10
b = 20

a, b = b, a

# 👉 This is packing + unpacking together

# 🧠 Visual Summary
# Packing:
x = 1, 2, 3

# 👉 many → one

# Unpacking:
a, b, c = x

# 👉 one → many

# Important:
# “Packing is assigning multiple values into a tuple, and unpacking is extracting those values into separate variables.”