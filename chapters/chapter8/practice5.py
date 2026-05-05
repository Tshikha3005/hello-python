words = ["motherfucker","shit","masturbate","wanker","dork"]

with open("content.txt","r") as f:
  content = f.read()

for word in words:
  new_content = content.replace(word, '#'  * len(word))

with open("content.txt","w") as f:
  f.write(new_content)