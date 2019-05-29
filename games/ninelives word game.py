# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:43:54 2019

@author: Aadhavan
"""

import random

lives = 3
words  = ['pizza', 'fairy', 'teeth', 'shirt']
secretword = random.choice(words)
clue = list('?????')
heartsymbol= u'\u2764'
guessedWordCorrectly = False

def updateClue(guessedLetter, secretword, clue):
    index = 0 
    while index < len(secretword):
        if guessedLetter == secretword[index]:
            clue[index] = guessedLetter
        index = index + 1
            
while lives > 0:
    print(clue)
    print('lives left: ' + heartsymbol * lives)

    print("secretword", secretword)
    guess = input("GUESS A LETTER OR THE WHOLE WORD:")
    if guess == secretword:
      guessedWordCorrectly = True
      break;
    
    if guess in secretword: 
        updateClue(guess, secretword, clue)
    else:
        print("incorrect. you lose a life")
        lives = lives - 1
if guessedWordCorrectly:
    print("YOU WIN !!!!!!!!", secretword, clue)
else: 
    print ("You lose")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    