import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 6
        #getting user input
    while len(word_letters) > 0 and lives > 0:
        #used letter
        user_letter = input("Guess a letter: ").upper()
        #what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current letter: ', ' '.join(word_list))

        print('You have', lives, 'lives left and you have used these letter: ',' '.join(used_letters))


        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1 #take away lives
                print('letter is not in word..')

        
        elif user_letter in used_letters:
            print('You have already used that character. Please try again!')

        else:
            print('Invalid character. Please try again! ')

    if lives ==0:
        print(f'You died. Sorry word is {word}')
    else:
        print('Yay! you guessed the word', word)
hangman()
