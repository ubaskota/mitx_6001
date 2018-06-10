#!/usr/bin/env python3

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Sat Feb 9 16:57:46 2017
    
    @author: Ujjwal
    """

def guess_the_number(low, high):
    print("please think of a number between 0 and 100.")
    count = 0
    while (low <= high):
        number = (low + high)//2
        logic = input("Is your secret number " + str(number) + " ?\n" + "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        if (logic == 'l'):
            low = number
            count = count + 1
        elif (logic == 'h'):
            high = number
            count = count + 1
        elif (logic == 'c'):
            return("Game over. Your secret number was: " + str(number))
            break
        else:
            print ("Sorry, I did not understand your input.")
            
print(guess_the_number(0, 100))
