import random
import time
import os

def play_again():
    loop = 'Do you want to play again? y = yes, n = no '
    play_game = input (loop)
    while play_game.lower()not in ['y','n']:
        play_game = input(loop)

    if play_game.lower() == 'y':
        return True
    else:
        return False

def hang_man(word):
    display = '_'*len(word)
    count = 0
    limit = 5
    letters = list(word)
    guessed = []
    while count < limit:
        guess = input(f'Hangman Word: {display} Enter your guess: \n').strip()
        while len(guess)== 0 or len(guess)>1:
            print('Invalid input. Enter a single letter\n')
            guess = input(f'Hangman Word: {display} Enter your guess:\n').strip()
        if guess in guessed:
            print('Oops! You already tried that guess, try again!\n')
            continue

        if guess in letters:
            letters.remove(guess)
            index = word.find(guess)
            display = display[:index] + guess + display[index + 1:]

        else:
            guessed.append(guess)
            count += 1
            if count == 1:
                time.sleep(1)
                print('   ______ \n'
                          ' |       | \n'
                          ' |       | \n'
                          ' |         \n'
                          ' |         \n'
                          '_|_\n')

                print(f'Wrong guess: {limit - count} guesses remaining\n')
            elif count == 2:
                time.sleep(1)
                print(' _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
                print (f'Wrong guess: {limit - count} guesses remaining \n')

            elif count == 3:
                time.sleep(1)
                print(' _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
                print(f'Wrong guess: {limit - count} guesses remaining\n')

            elif count == 4:
                time.sleep(1)
                print('   _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     O \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n')
                print(f'Wrong guess: {limit - count} guesses remaining\n')

            elif count == 5:
                time.sleep(1)
                print(' _____ \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     | \n'
                    '  |     O \n'
                    '  |    /|\ \n'
                    '  |    / \ \n'
                    '__|__\n')
                print(f'Wrong guess. You\'ve been hanged!\n')
                print(f'The word was: {word}')

        if display == word:
            print (f'Congratulations! The word \'{word}\' is correct!')
            break
def play_hangman():
    print('\nWelcome to Hangman\n')
    name = input('Enter your name: ')
    print(f'Good luck {name}!')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    words_to_guess = [
        'animal' , 'brave' , 'piano' , 'scheme' , 'anchor', 'mountain',
        'forest' , 'bannana', 'courtesy', 'quote', 'absurd', 'luxury' ,
        'bikini' , 'blitz', 'awkward', 'pixel', 'pneumonia', 'glamour'
        ]
    play = True
    while play:
        word = random.choice(words_to_guess)
        hang_man(word)
        play = play_again()

    print('Thanks for playing!')
    exit()

if __name__== '__main__':
    play_hangman()

    













    
            
