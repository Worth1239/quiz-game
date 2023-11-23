import time

print("Hello, welcome to my quiz game about me!")
play = input("Would you like to play? ")
if play.lower() == "yes":
    print("Okay! Lets start")
else:
    quit()
score = 0
print("First Question!")
answer = input("What is my name? ")
if answer.lower() == "alejandro":
    print("Correct!")
    score += 1
else:
    print("Incorrect, my name is alejandro")
print("Question Two")
answer = input("What grade am I in? ")
if answer == "9":
    print("Correct!")
    score += 1
else:
    print("Incorrect, I am in 9th grade ")
print("Question Three!")
answer = input("How old am I? ")
if answer == "15":
    print("Correct!")
    score += 1
else:
    print("Incorrect, I am 15 years old")
print("Question Four!")
answer = input("What is my favorite color? ")
if answer.lower() == "green":
    print("Correct!")
    score += 1
else:
    print("Incorrect, my favorite color is green")
print("Question Five!")
answer = input("What language do I take? ")
if answer.lower() == "japanese":
    print("Correct!")
    score += 1
else:
    print("Incorrect, I take Japanese")
print("Question Six!")
answer = input("What nationality am I? ")
if answer.lower() == "mexican":
    print("Correct!")
    score += 1
else:
    print("Incorrect, I am mexican ")
print("That is the end of our quiz! Let's see what you got")
time.sleep(3)
print("You got a score of " + str(score) + " out of six!")
print("That is " + str((score/6) * 100) + "%")
