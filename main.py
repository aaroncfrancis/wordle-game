import random
import string

def generate_word():
    """generates a random 5-letter word"""
    word = ''.join(random.sample(string.ascii_lowercase,5))
    return word

def play_wordle():
    """initialize target word by calling generate word and initialize guess"""
    target_word = generate_word()
    num_guess = 0

    while True: 
        guess = input('First guess (5 letter word): ')
        if len(guess) !=5:
            print('Your guess must be 5 letters long! ')
            continue
            
        if guess == target_word:
            print(f"Success! You guessed the correct word in {num_guess} tries")
            break

        feedback = []
        for i in range(5):
            if guess[i] == target_word[i]:
                feedback.append(str(target_word[i])) #need help here*
            elif guess[i] in target_word:
                feedback.append('_')
            else:
                feedback.append('x')

        print(''.join(str(x) for x in feedback))

play_wordle()