# for i in range(1,101):
#   print(i)

li = [1, "Harry",False,"This","Rohan","Shubham","Shubhi"]

for i in range(len(li)):
  print(li[i])
# range function is used to generate a sequence of number
# range(Start, stop, step_size)

for i in range(0,7,2):
  print(i)

l = [1,4,6,234,6,764]

for i in range(len(l)-1, -1, -1):
  print(l[i])

t=(6,231,75,122) #tuple
for i in t:
  print(i)
else:
  print("done")
# for with else  # 
# for loop will continue until it gets value otherwise when it exhausts it go to else

for i in range(0,20):
  if i == 14:
    break #Exit the loop right now so it will print till 14
  print(i)

for i in range(0,20):
  if i == 14:
    continue #Skip this loop right now so it will print everything except 14
  print(i)

# pass is a null statement in python | it instructs to "do nothing"
l = [1,7,8]
for item in l:
  pass