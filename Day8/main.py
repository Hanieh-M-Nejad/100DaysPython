# Prime number checker first method
from math import sqrt

### getting input from user
valid_number = False
while not valid_number:
    user_num = int(input("Type a number to check if it is a Prime number!: "))
    if (user_num > 0):
        valid_number = True

### checking if it's prime
prime = []
for i in range (2, int(sqrt(user_num)+1)):
    if user_num % i == 0:
        prime.append(i)


if len(prime)==0:
    print("It's a prime number!")
elif len(prime)>0:
    print(f"This number is NOT a prime number! It is divisible by {str(prime)[1:-1]}.")

