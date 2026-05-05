f = open("file.txt")
print(f.read())
f.close()
# the same can bew ritthen in using with statement
with open("file.txt") as f:
  print(f.read())
  # you dont have to explicity close the file