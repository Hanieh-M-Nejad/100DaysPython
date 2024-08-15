import random
from art import stages, logo
import words
print(logo)
#choosing and showing the length of the word
word_list = words.word_list
chosen_word = random.choice(word_list)
display = []
for i in chosen_word:
    display.append("-")



end_of_game = False
lives = 6
guess_list = []
while not end_of_game:
    print(display)
    user_guess = input("All right! Guess a letter. ").lower()
    if user_guess in guess_list:
        print("You already tried that!")
    else:
        guess_list.append(user_guess)
        for i in range(0, len(chosen_word)):
            if user_guess == chosen_word[i]:
                display[i] = user_guess
        if user_guess not in chosen_word:
            lives -= 1
            print(stages[lives])
        if "-" not in display:
            end_of_game = True
            print("Congrats! You Won!")
        if lives == 0:
            end_of_game = True
            print("Sorry! You Lost!")
            print(f"The word was {chosen_word}")

