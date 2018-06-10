#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Sat Feb 6 14:57:46 2017
    
    @author: Ujjwal
    """

# Problem 2
# (10/10 points)
# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your
# program should print
# Number of times bob occurs is: 2

# Paste your code into this box

def count_bob(s):
    count = 0
    for i in range(len(s)-2):
        if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
            count = count + 1
        else:
            pass
    return count
print (count_bob(s))
        
