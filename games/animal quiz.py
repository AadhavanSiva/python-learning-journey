# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 12:04:56 2019

@author: Aadhavan
"""
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct')
            score = score + 1  
            still_guessing = False
        else:
            if attempt < 2:
                guess =  input('Sorry wrong answer. Try again')
            attempt += 1
    if attempt == 3:
        print ('The correct answer is', answer) 
score = 0
print('Guess the animal!')
guess1 = input('Which bear lives at the North pole')
check_guess(guess1, 'polar bear')
guess2 = input('Which is the fastest living land animal')
check_guess(guess2, 'cheetah')
guess3 = input('Which is the largest animal')
check_guess(guess3, 'blue whale')

print ('Your score is', score, '/3')