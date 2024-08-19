# secret auction with lists

print("Welcome to the secret auction program.")
bidders_list = []
bids_list = []
end_auction = False
while not end_auction:
    bidder = input("What is your name? ")
    bid = float(input("What is your bid? $"))
    bidders_list.append(bidder)
    bids_list.append(bid)
    should_cont = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_cont == "no":
        end_auction = True

#find index max bids
i = bids_list.index(max(bids_list))
winner = bidders_list[i]
winner_bid = max(bids_list)
print(f"The winner is {winner} with a bid of ${winner_bid}.")