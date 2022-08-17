#computer generated random number 
import random

def guess(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Guess from 1 to {x}: "))
        if guess < random_num:
            print("Try again, too low!")
        elif guess > random_num:
            print("Try again, too high!")
    print(f"Congrats. You guessed {random_num} Correctly!")


guess(15)
