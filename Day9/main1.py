# secret auction with dictionary

print("Welcome to the secret auction program.")
bids_dic = {}
end_auction = False
while not end_auction:
    bidder = input("What is your name? ")
    bid = float(input("What is your bid? $"))
    bids_dic[bidder] = bid
    should_cont = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_cont == "no":
        end_auction = True
    else:
        print("\n" * 91)


#find index max bids
def find_winner(bids_dic):
    highest_bid = 0
    winner = ""
    for i in bids_dic:
        bid_amount = bids_dic[i]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = i
    return winner, highest_bid

winner, winner_bid = find_winner(bids_dic)
print(f"The winner is {winner} with a bid of ${winner_bid}.")