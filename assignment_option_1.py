# Scout Crooke, 10/21/19, This program runs a guessing game


import random

while True:
    question = input("Do you want to play this guessing game? (yes or no)")
    if question == "no":
        print("Alright, see you later!")
        break
    elif question == "yes":
        num = random.randint(1, 100)
        print("Great lets play! Guess a number between 1 and 100")
        guess = int(input("What is your number guess?"))
        if guess > num:
            print("Your number is to high")
            guess = int(input("Guess again!"))
        elif guess < num:
            print("Your number is too low")
            guess = int(input("Guess again!"))
        elif guess == num:
            print("Awesome! You guessed my number?")
        break


