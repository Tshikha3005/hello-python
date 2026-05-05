# with open('file.txt', 'r') as f:
#   content = f.read()
# if "python" in content:
#   print("Yes my lord")


# practive 7
with open('file.txt', 'r') as f:
  lines = f.readlines()
lineno = 1
for line in lines:
  if 'python' in line:
    print(line)
    break
    lineno += 1
  else:
    print("not found")
