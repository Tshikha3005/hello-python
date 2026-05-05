#write a program to accept marks of 6 students and display in sorted manner


marks_list = []
for i in range(6):  
  s = int(input('Enter marks ${i}'))
  marks_list.append(s)
  marks_list.sort()  
print(marks_list)