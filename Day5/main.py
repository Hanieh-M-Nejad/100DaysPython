import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters = int(input("How many letters you like in your password?"))
num_symbols = int(input("How many symbols you like in your password?"))
num_numbers = int(input("How many numbers you like in your password?"))

password_list = []
for i in range (0, num_letters):
    chosen_let = random.choice(letters)
    password_list.append(chosen_let)

for i in range(0, num_symbols):
    chosen_sym = random.choice(symbols)
    password_list.append(chosen_sym)

for i in range (0, num_numbers):
    chosen_num = random.choice(numbers)
    password_list.append(chosen_num)

pass_shuffled = random.shuffle(password_list)

password = ""
for i in password_list:
    password += i


print(f"Here is your password: {password}")