import random

#user
user = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))



#pc
rps_list = ["Rock", "Paper", "Scissors"]
pc = random.choice(rps_list)
pc_index = rps_list.index(pc)

emojis = ["🪨", "📃", "✂️"]
print(f"Your choice: {emojis[user]}")
print(f"Cpmputer's choice: {emojis[pc_index]}")



if user == pc_index:
    print("Draw!")
elif user == 0:
    if pc_index == 2:
        print("You Won!")
    else:
        print("You Lost!")
elif user == 1:
    if pc_index == 0:
        print("You Won!")
    else:
        print("You Lost!")
elif user == 2:
    if pc_index == 1:
        print("You Won!")
    else:
        print("You Lost!")
else:
    print("Your choice was invalid. You Lost!")