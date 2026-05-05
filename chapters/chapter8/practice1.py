f = open("poems.txt", 'r')
data = f.read()
print(data)
if 'Twinkle' in data:
  print("Hell yaaa")
f.close()