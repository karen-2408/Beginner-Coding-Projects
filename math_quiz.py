import math
import time

print("Welcome to my math quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0
questions = 10

for i in range(questions):
  num1 = random.randint(0, 10000)
  num2 = random.randint(0, 10000)
  answer = input("What does " + num1+ "+ " + num2)
  real_answer = num1+num2
  if answer == real_answer:
    print('Correct!')
    score += 1
  else:
    print("Incorrect!")

  if i < questions - 1:
    print("Next question coming in 10 seconds...\n")
    time.sleep(10)

print("Quiz complete!")
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
