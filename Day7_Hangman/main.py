#Step 1
import random
from turtle import clear

import hangman_words
import hangman_art
# Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(hangman_words.word_list)
# Set 'lives' to equal 6.
lives = 6
#print logo
print(f"{hangman_art.logo}")
# Check world
print(f'Pssst, the solution is {chosen_word}.')
# Create an empty List called display.
display = []
#For each letter in the chosen_word, add a "_" to 'display'.
num_letter = 0
len_word = len(chosen_word)
for _ in range(len_word):
    display.append("_")
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
print(display)
# Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won
end_of_game = False

while not end_of_game:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()
    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print("You have already guess in this word")
    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for n in range(len_word):
        letter = chosen_word[n]
        if guess == letter:
            display[n] = guess
    # If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop, it should print "You lose."
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f"You guessed {guess}, sorry is  wrong letter, you lost 1 lives, only {lives} left")
    print(display)
    # Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    # from hangman_art import stages (import kieu 2)
    print(f"{hangman_art.stages[lives]}")

    if lives == 0:
        end_of_game = True
        print("YOU LOSE.")

    if "_" not in display:
        end_of_game = True
        print("YOU WIN")
