import random
#A while loop makes a section of code repeat until a certain condition is met. 
#In this exercise, you will create a Python script that asks the user to correctly guess a number.
print("Welcome to Guess the Number")
print("The rules are simple, I will think of a number and you guess the number")
number= random.randint(1,10)

isGuessRight= False 
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess)== number:
        print("You guessed {}. That is correct. You Win! " .format(guess))
        isGuessRight= True
    else:
        print("You guess {}. Sorry that is incorrect. Try again" .format(guess))
 