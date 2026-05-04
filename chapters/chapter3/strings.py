# sequence of charaters enclised in quotes
#  stieng ins immutable we cant change something in string once it is created but we can create a new string by concatenating two strings or by slicing a string.
a = 'harry' # string can be defined in single or double quotes
a = "harry" # if we want to use single quote in string then we can use double quotes to define string
a = '''harry''' # if we want to use both single and double quotes in string then we can use triple quotes to define string

# string slicing
a = "harry" 
print(a[0]) # h

print(a[0:3]) # harry[0:3] means we want to get the characters from index 0 to index 2 (3-1) which is 'har'
print(a[:3]) # this is same as a[0:3]
print(a[-4:-1]) # this will give us 'arr' because -4 means we want to start from the 4th last character and -1 means we want to end at the last character (not including the last character)
print(a[:-1])
print(a[-1:])
print(a[-1:1])


# slicing with skip value
word = 'amazing'
print(word[1:6:2]) # this will give us 'mzn' because we are starting from index 1 and ending at index 5 (6-1) and we are skipping 2 characters in between  
print(word[:7])

# string functions
print(len(word)) # this will give us the length of the string which is 7
print(word.upper()) # this will give us the string in uppercase which is 'AMAZING'
print(word.lower()) # this will give us the string in lowercase which is 'amazing'
print(word.capitalize
      ()) # this will give us the string with the first character in uppercase and the rest in lowercase which is 'Amazing'
print(word.replace('a', 'o')) # this will replace all the occurrences of 'a' with 'o' which is 'omozing' change all occurences
print(word.endswith('g')) # this will return True if the string ends with 'g' which is True
print(word.startswith('a')) # this will return True if the string starts with 'a' which is True
print(word.find('z')) # this will return the index of the first occurrence of 'z' which is 4

