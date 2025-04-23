#Build a Number guessing game, in which the user selects a range.
# Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# Some random integer will be selected by the system and the user has to guess that
# integer in the minimum number of guesses

import random


def is_valid_input(input_text):
    if input_text.isdigit():
        return True
    else:
        return False


print("---Welcome the game of Number guessing."
      "Input your lower and upper range to play the guessing game.---\n")

# check input validitity
start = input("Enter Start range: ")
if not is_valid_input(start):
    print("Range value should be a positive number")
else:
    end = input("Enter End range: ")
    if not is_valid_input(end):
        print("Range value should be a positive number")
    else:
        start_range = int(start)
        end_range = int(end)


        number_to_be_guessed = random.randint(start_range,end_range)
        no_of_guesses = 0  # counter to keep track of guesses

        print("\n.......The Guessing Game Begins now........")

        while True:
            guessed_num = int(input("\nGuess the number: "))
            no_of_guesses += 1

            if guessed_num == number_to_be_guessed:
                print(f"\nCongratulations! \nTotal number of guesses = {no_of_guesses}.")
                break
            else:
                if guessed_num > number_to_be_guessed:
                    print("Try again! You guessed too high.")
                else:
                    print("Try again! You guessed too small.")


