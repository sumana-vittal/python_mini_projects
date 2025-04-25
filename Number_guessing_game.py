#Build a Number guessing game, in which the user selects a range.
# Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# Some random integer will be selected by the system and the user has to guess that
# integer in the minimum number of guesses

import random

# Function to check if user has given valid input.
def is_valid_input(input_text):
    if input_text.isdigit():
        return True
    else:
        return False


print("---Welcome the game of Number guessing."
      "Input your lower and upper range to play the guessing game\n"
      "You have 7 chances to guess. Good Luck!!---\n")

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

        if start_range < end_range:
            print("\n...Start Range should be greater than End range....")

        else:
            no_of_chances = 7 # user has to guess within 7 chances
            number_to_be_guessed = random.randint(start_range,end_range)
            no_of_guesses = 0  # counter to keep track of guesses

            print("\n.......The Guessing Game Begins now........")

            while True:
                if no_of_guesses == no_of_chances:
                    print(f"Couldn't guess in {no_of_chances} turns. \nBetter Luck new time...")
                    break

                guessed_num = int(input("\nGuess the number: "))
                no_of_guesses += 1

                if guessed_num == number_to_be_guessed:
                    print(f"\nCongratulations!  You Got it!! \nTotal number of guesses = {no_of_guesses}.")
                    break
                else:
                    if guessed_num > number_to_be_guessed:
                        print(f"\nTry again.. {no_of_chances-no_of_guesses} turns Left ! \n.... CLUE: You guessed too high.")
                    else:
                        print(f"\nTry again.. {no_of_chances-no_of_guesses} turns Left! \n.... CLUE: You guessed too small.")



