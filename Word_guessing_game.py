# This program is a simple word-guessing game where the user
# has to guess the characters in a randomly selected word within a
# limited number of attempts. The program provides feedback after
# each guess, helping the user to either complete the word or lose
# the game based on their guesses.

import random

print("\n.....Welcome to the GUESSING WORD GAME!! ....")


# List of words to be guessed
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# selects the random word from the list.
word_to_guess = str(random.choice(words))

print(f"\nYou get '{len(word_to_guess)+5}' attempts to get your guessing.")

chances_to_guess = len(word_to_guess) + 5 # no. of attempts user gets.

guess_counter = 0  # counter to keep track of guesses

# print(word_to_guess)
user_progress = []

for i in range(0, len(word_to_guess)):
    user_progress.append("_")
print(user_progress)

ind_list = [] # list to keep track of index

while True:
    user_guess = input("\nGuess a character : ").lower()
    guess_counter += 1

    if user_guess in word_to_guess:
        #get all the indexes, in the list.
        ind_list = [pos for pos,c in enumerate(word_to_guess) if user_guess == word_to_guess[pos]]

        # replace the right words with the progress list.
        for i in ind_list:
            user_progress[i] = user_guess

        #print the updated list
        print(user_progress)
    else:
        print(f"\n.....you have {chances_to_guess-guess_counter} attempts left....")

    # if user is not able to guess before the given attempts, then he lose.
    if chances_to_guess == guess_counter:
        print("\n...Better luck next time!...")
        print(f"\n ...The word is '{word_to_guess}'......")

        break

    # if user is able to guess before all attempts , then he wins
    if "".join(user_progress) == word_to_guess:
        print("\n....Congratulations! You Win!....")
        break













