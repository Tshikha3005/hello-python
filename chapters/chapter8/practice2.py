import random

def game():
  print("You are playing the game..")
  score = random.randint(1, 62)
  with open("hi-score.txt") as f:
    hiscore = f.read()
    if hiscore != '':
      hiscore = int(hiscore)
    else:
      hiscore = 0
  if score > hiscore:
    with open("hi-score.txt", "w") as f:
      f.write(str(score))
  print(f"score {score}")
  
game()
