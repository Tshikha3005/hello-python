# Snake, Water and gun

'''
1 snake
-1 water
0 for gun
'''
import random

computer = random.choice([-1,0,1])
you = (input("Enter your choice:"))
youDict ={
  "s":1,
  "w":-1,
  "g":0
}

younum = youDict[you]
if(computer == you):
  print("Its a draw")
else:
  if(computer == -1 and younum == 1):
    print("You win")
  elif(computer == -1 and younum == 0):
    print("Lose")
  elif(computer == 1 and younum == -1):
    print('you loss')
  elif(computer == 1 and younum == 0):
    print("you lose")
  elif(computer == 0 and younum == -1):
    print("you win")
  elif(computer == 0 and younum == 1):
    print("you lose")
  else:
    print("Somethign went wrong")