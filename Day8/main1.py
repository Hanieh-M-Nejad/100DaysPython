# Prime number checker second method
from math import sqrt

### getting input from user
def prime_checker(number):
    ### checking if it's prime
    prime_number = True
    for i in range (2, int(sqrt(number)+1)):
        if number % i == 0:
            prime_number = False


    if prime_number == True:
        print("It's a prime number!")
    else:
        print("It's not a prime number!")

prime_checker(130)