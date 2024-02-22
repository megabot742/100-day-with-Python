import random
from art import logo
from art import vs
from game_data import data

# Print logo
print(logo)
score = 0
account_b = random.choice(data)

game_continue = True
while game_continue:
    def format_data(account):
        # Format the account data into printable format.
        account_name = account["name"]
        account_descr = account["description"]
        account_country = account["country"]
        return f"{account_name}, a {account_descr}, from {account_country}"

    def check_answer(guess, a_follower, b_follower):
        # Use if statement to check if user is correct
        if a_follower > b_follower:
            return guess == "a"
        else:
            return guess == "b"


    # Generate a random account from the game data.
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who have more follow? Type 'A' or 'B': ").lower()

    # Check if user is correct
    # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    print(f"------------------------------------------------------")
    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You right, Current score: {score}")
    else:
        game_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")