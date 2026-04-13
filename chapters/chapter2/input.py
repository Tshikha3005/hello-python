import os

directory_path = input("Enter the directory path: ")

contents = os.listdir(directory_path)
for listed_item in contents:
  print(listed_item)