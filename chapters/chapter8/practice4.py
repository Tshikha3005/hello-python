with open("animals.txt", 'r') as f:
  content = f.read()

content_new = content.replace("Donkey","#####")
with open("animals.txt",'w') as f:
  content = f.write(content_new)