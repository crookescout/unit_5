# Scout Crooke, 10/21/19, This program runs a guessing game

import random

tries = 0
while True:
    # This loop allows you to play the game multiple times
    question = input("Do you want to play this guessing game? (yes or no)")
    if question == "no":
        print("Alright, see you later!")
        break
    elif question == "yes":
        num = random.randint(1, 100)
        print("Great lets play! Guess a number between 1 and 100")
        while True:
            # This loop gives the user hints if their number guess is too high or too low and
            # counts the number of guesses it takes them to guess the correct number
            guess = int(input("What is your number guess?"))
            tries += 1
            if guess > num:
                print("Your number is to high")
            elif guess < num:
                print("Your number is too low")
            elif guess == num:
                print("Awesome! You guessed my number in", tries, "guesses!")
                break
