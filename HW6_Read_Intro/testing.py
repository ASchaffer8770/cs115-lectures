##Lecture examples

#If/else statement
age = 30
age2 = 15

if age > 21:
  print("You are an adult")
  print("You're old")
else:
  print("You're still a kid")

##Example of else if ordering matters.
"""
Whenever the condition is met, code exits the if
statement block, if eval == false then code continues to run
"""
difference = age - age2
if difference >= 0:
  print("Positive or zero")
elif difference > 5:
  print("big number")
elif difference < 0:
  print("negative")

if difference > 5:
  print("big number")

##Loops!!!
##while loop
counter = 0
while counter <= 10:
  print(counter)
  ##counter incrementation
  counter += 1

#for loop
inventory = ['sword', 'shield', 'key']

for item in inventory:
  print(item)

#boolean operators
isGamePaused = False
isDead = True
if isGamePaused or isDead:
  print("Game Paused")
else:
  print("Game in progress")
#Both conditions need to be true to exe
if isGamePaused and isDead:
  print("Game Over")

health = 50
if health == 0:
  #== is evaluating the variable
  #= is assigning the variable
  isDead = True

