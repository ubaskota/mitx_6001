#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Sat Feb 5 14:57:46 2017
    
    @author: Ujjwal
    """
# Problem 1
# (10/10 points)
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

# Paste your code into this box

def count_vowel(s):
    vowels = ['a','e','i','o','u']
    count = 0
    for i in s:
        if i in vowels:  #if a letter is in the vowels list
            count = count + 1   # increment the count by one
    return count
 
print(count_vowel(s))
            
