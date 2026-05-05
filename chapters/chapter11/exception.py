# try:
#   a = int(input("Hey, Enter a number"))
#   print(a)
# except Exception as e:
#   print(e)

# print("Thank you")

# Exception handling in Python is a process used to handle errors that occur during the execution of a program (runtime errors). Instead of the program crashing, you can "catch" these errors and respond to them gracefully.

try:
    num = int(input("Enter a number: "))
    print(100 / num)
except ValueError:
    print("Error: Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Key Components of Exception Handling
# Component Purpose
# try       Contains the code you want to test for errors.
# except    Handles specific errors (like ValueError, IndexError, etc.).
# else      Runs code only if no exceptions were raised in the try block.
# finally   Runs no matter what, even if the program crashes or returns early. Often used for "cleanup" (like closing a file).

list1 = [10, 20, 30]
try:
    print(list1[5]) # Index 5 does not exist
except IndexError:
    print("The index you are looking for is out of range.")

# ValueError: Right type, but wrong value (e.g., int("abc")).

# TypeError: Wrong type entirely (e.g., len(5)).

# IndexError: Trying to access a list index that doesn't exist.

# KeyError: Trying to access a dictionary key that isn't there.

# ZeroDivisionError: Dividing by zero.

# FileNotFoundError: Trying to open a file that doesn't exist on your disk.

# AttributeError: Trying to call a method that doesn't exist for that object (e.g., calling .append() on a string).

a = int(input('Enter a number'))
b = int(input('Enter second number'))

if b == 0:
    raise ZeroDivisionError("Hey our program is not meant to divide by number 0")
print(f"Thie diviviosn a/b is {a/b}")

# try with else
# else will call only when try run successfully 

try:
  a = int(input('Enter a number'))
  print(a)
except Exception as e:
  print(e)
else:
  print("Hello")
finally: #it will come in use in function
   print("Uff Finally")
