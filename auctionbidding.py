
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    max(bidding_dictionary)
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

bids = {}

continue_bidding = True
while continue_bidding:
    name = input("what is your name?: ")
    price = int(input("how much was the bid?: $"))
    bids[name] = price
    should_continue = input("ARE there any other person in bidding? 'yes' or 'no' \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)                       
    else:
        should_continue == "yes"
        print("\n" * 20)
