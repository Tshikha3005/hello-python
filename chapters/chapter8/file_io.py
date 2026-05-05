# FILE/IO: Random accessmemory is volatie, and all its content are lost once a program terminated in order to persist the data forever, we use files.
# A file is data stored in a storage device. A python program can talk to the file by reading content from it and writing content to it.

# RAM=> Volatile | HDD=> Non volatile
# Types of files: 1) Text files(.txt, .c etc) 2) Binary Files(.jpg, .dat etc)
# python has a lot of fucntions for reading, updating and deleting files
# for opening a file open("filename","mode of opening(Read mode)")
# open("this.txt", "v")

# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()

# modes for opening file: 
#   r => open for reading/
#   w => open for writing/
#   a => open for appending/
#   + => open for updating/
#   'rb' => will open for read in binary mode/
#   'rt' => open for read in text mode

st = "Hey Shikha, are you still trying for the opening?"
f = open("file.txt","a") #i did used w to wirte it overrides the file, now used a to append
f.write(st)
f.close()

new_f = open("file.txt")

data = new_f.read()
print(data)
f.close()

# f.readline() => Read one line from the file
fread = open('file.txt')
# lines = fread.readlines()
# print(lines, type(lines))
line = fread.readline()
while(line != ''):
  print(line)
  line = fread.readline()
f.close()