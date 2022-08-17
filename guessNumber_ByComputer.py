#we will keep our number secret and let the computer guess the right number and we will tell is it low, high or correct!

import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else: 
            guess = low 
        feedback = input(f"Is {guess} is high(h), low(l), correct(c)!: ").lower()
        if feedback == 'h':
            high = guess-1
        elif feedback == "l":
            low = guess+1  
    print(f"yay.congrats the computer guessed {guess},correctly!")

computer_guess(20)
