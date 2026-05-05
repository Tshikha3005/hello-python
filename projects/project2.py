# PErfect Guess

import random
n = random.randint(1,100)
a = -1
guesses = 0
while (a != n):
  a = int(input("Guess the number: "))
  if a < n:
    print('Guess the number higher')
    guesses += 1

  else:
    print("Guess the lower no")
    guesses += 1

print(f"You have guessed the number correctly in {guesses}")
    