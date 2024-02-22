import random
from art import logo
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
# Create a function called calculate_score() that takes a List of cards as input
# #and returns the score.
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
# Create a function called compare() and pass in the user_score and computer_score.
# If the computer and user both have the same score, then it's a draw.
# If the computer has a blackjack (0), then the user loses.
# If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses.
# If the computer_score is over 21, then the computer loses.
# If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"
def play_game():
    print(logo)
    # Deal the user and computer 2 cards each using deal_card()
    user_cards = []
    computer_cards = []
    is_game_over = False

    for item in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    # The score will need to be rechecked with every new card drawn and the checks to be repeated until the game end
    while not is_game_over:
        # Call calculate_score(). If the computer or the user has a blackjack (0)
        # if the user's score is over 21, then the game ends
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your card: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            #  If the game has not ended, ask the user if they want to draw another card.
            go_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            #  If the game has not ended, ask the user if they want to draw another card.
            if go_continue == 'y':
                user_cards.append(deal_card())
            #  If no, then the game has ended
            else:
                is_game_over = True

    # Once the user is done, it's time to let the computer play.
    # Check score before drawing cards
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    # The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final card: {user_cards}, current score: {user_score}")
    print(f"Computer's final card: {computer_cards}, current score: {computer_score}")
    print(compare(user_score, computer_score))
# Ask the user if they want to restart the game.
# If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    play_game()