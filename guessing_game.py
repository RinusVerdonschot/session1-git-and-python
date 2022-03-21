from random import randint  # Import the randint function from the random package
# import random

number = randint(1, 100)  # Generate a random number between 1 and 10
print(number)  # Print the number (to make testing easier)

# Ask the user for a guess, and convert the result to an integer
guess = int(input('Guess the number (between 1 and 100): '))

# While the correct number was not guessed...
while number != guess:
    if guess-number > 0: 
        guess = int(input('Try again, but lower: '))  # Gve feedback and ask them to guess again
    else:
        guess = int(input('Try again, but higher: '))  # Give feedback and ask them to guess again
    
# When the above while loop terminates, that means the correct number was guessed!
print('Correct!')

# Homework: extend the above program so that:
#   1) it generates a number between 1 and 100, -> DONE
#   2) it gives higher/lower feedback on an incorrect guess. -> DONE