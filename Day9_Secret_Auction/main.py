import replit

import art

print(art.logo)
print("Welcome to the secret auction program")
def find_highest_bidder(bidding_record):
  max_bid = 0
  winner = ""
  # Bidding_record = {"Angela": 123, "James": 321}
  for key in bidding_record:
    bid_amount = bidding_record[key]
    if bid_amount > max_bid:
      max_bid = bid_amount
      winner = key
  print("------------------------------------------------------------------")
  print(f"The winner is {winner} with a bid of ${max_bid}")
bids = {}
check = False
while not check:
    print("------------------------------------------------------------------")
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    continue_auction = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    bids[name] = price         # Create dictionary
    max_price = 0
    if continue_auction == "no":
        find_highest_bidder(bidding_record=bids)
        check = True
    # elif continue_auction == "yes":
    #     replit.clear()


