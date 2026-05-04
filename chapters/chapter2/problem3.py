a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print("The average is: ", (a + b)/2) # this will not give the correct average because of operator precedence, it will divide b by 2 first and then add a to it. To get the correct average, we need to use parentheses to change the order of operations. The correct code should be: print("The average is: ", (a + b) / 2)