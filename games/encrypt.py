# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:26:08 2019

@author: Aadhavan
"""

from tkinter import messagebox, simpledialog, Tk

def is_even(number):
    return number % 2 == 0

def get_task():
    task = simpledialog.askstring('task', 'Do you want to encrypt or decrypt?')
    return task

def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message')
    return message


def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters
        
def get_odd_letters(messsage):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    

    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    print("even_letters", even_letters)
    print("odd_letters", odd_letters)
    for counter in range (0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message =  ''.join(letter_list)
    return new_message

root = Tk()

while True:
    task = get_task()
    if task == 'encrypt':
        message = get_message()
        encrypted = swap_letters(message)
        messagebox.showinfo('Ciphertext of the  secret message is', encrypted)
    elif task == 'encrypt':
        message = get_message()
        decrypted = swap_letters(message)
        messagebox.showinfo('Message to decrypt is:', decrypted)
    else:
        break;
root.mainloop()
