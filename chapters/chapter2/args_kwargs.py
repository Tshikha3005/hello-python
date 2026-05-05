def main():
  testfunc(1,2,3,4,5,6,one=1, two=2, three=3)

def testfunc(nu, anu, othu, *args, **kwargs):
  print(nu, anu, othu, args, kwargs)
  for k in kwargs:
    print (k, kwargs[k])

# here: 
# nu => 1
# anu => 2
# othu => 3
# *args => 4,5,6
# **kwargs => one=1, two=2, three=3

# What are *args and **kwargs?

# They let a function accept variable number of arguments

# 🔥 1. *args (Non-keyword arguments)

# 👉 Collects extra positional arguments into a tuple

def add(*args):
    print(args)

add(1, 2, 3)

# 👉 Output:

(1, 2, 3)
# ✅ Example
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10
# 🧠 Think:

# *args = “I don’t know how many values you’ll pass”

# 🔥 2. **kwargs (Keyword arguments)

# 👉 Collects named arguments into a dictionary

def print_info(**kwargs):
    print(kwargs)

print_info(name="Shikha", age=25)

# 👉 Output:

{'name': 'Shikha', 'age': 25}
# ✅ Example
def user_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
# 🧠 Think:

# **kwargs = “I don’t know what keys you’ll pass”

# 🔥 3. Using both together
def demo(a, *args, **kwargs):
    print("a:", a)
    print("args:", args)
    print("kwargs:", kwargs)

demo(1, 2, 3, x=10, y=20)
# 🧠 Order rule (VERY IMPORTANT)
def func(normal, *args, **kwargs):
  pass
# 👉 Order must be:

# normal → *args → **kwargs
# 🔥 4. Unpacking (reverse of collecting)
# Tuple → arguments
nums = (1, 2, 3)

def add(a, b, c):
    return a + b + c

print(add(*nums))
# Dict → keyword arguments
data = {"name": "Shikha", "age": 25}

def show(name, age):
    print(name, age)

show(**data)
# 💀 Interview Traps
# 🔴 Trap 1
def func(*args):
    print(type(args))

# 👉 tuple ✅

# 🔴 Trap 2
def func(**kwargs):
    print(type(kwargs))

# 👉 dict ✅

# 🔴 Trap 3
func(1, 2, name="x")

# 👉 args = (1,2)
# 👉 kwargs = {"name": "x"}

# 🧠 Real Use Cases
# 🔹 FastAPI / frameworks
def route_handler(*args, **kwargs):
   pass
# 🔹 Decorators
def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
# 🔹 Flexible APIs
def create_user(**data):
   pass
# 🎯 Interview Answer

# “*args collects positional arguments into a tuple, and **kwargs collects keyword arguments into a dictionary, allowing functions to accept variable inputs.”