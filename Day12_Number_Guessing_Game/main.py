import random
EASY_LEVEL = 10
HARD_LEVEL = 5
# Make function to check user's guess against actual answer.
def check_answer(guess, number, turn):
    if guess > number:
        print(f"To high")
        return turn - 1
    elif guess < number:
        print(f"To low")
        return turn - 1
    elif guess == number:
        print(f"Well done,correct number is {number}")

# Make function to set difficulty.
def set_difficulty():
    level = input(f"Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL
    elif level == "hard":
        return HARD_LEVEL
# Main game function
def game():
    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")
    # Choosing a random number between 1 and 100
    number = int(random.randrange(1, 100))
    # Check
    # print(f"{number}")
    turn = set_difficulty()
    guess = 0
    while guess != number:
        print(f"You have {turn} remaining to guess the number.")
        # Let the user guess a number.
        guess = int(input(f"Make a guess: "))
        turn = check_answer(guess, number, turn)
        if turn == 0:
            print("You're run out guess, you lose")
            return
game()