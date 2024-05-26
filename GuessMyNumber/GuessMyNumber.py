# Build a Number guessing game, in which the user selects a range.
# Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses
import random
import math

game_title = "Guess My Number"
print("Welcome to", game_title)

# Taking inputs with error handling
while True:
    try:
        lower = int(input('Enter Lower range:- '))
        upper = int(input('Enter Upper range:- '))
        break
    except ValueError:
        print("Please enter valid integers for the ranges.")

# generating random number between the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ", 
       round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0
success = False
 
# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1
 
    # taking guessing number as input
    while True:
        try:
            guess = int(input("Guess a number:- "))
            break
        except ValueError:
            print("Please enter a valid integer.")
 
    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        success = True
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too low!")
    elif x < guess:
        print("You Guessed too high!")

# Shows this output If Guessing is more than required guesses.
if count >= math.log(upper - lower + 1, 2) and not success:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")