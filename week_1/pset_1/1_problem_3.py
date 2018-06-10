#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Sat Feb 6 14:57:46 2017
    
    @author: Ujjwal
    """
# Problem 3

# (15/15 points)
# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if
# s = 'azcbobobegghakl', then your program should print:
# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print:
# Longest substring in alphabetical order is: abc

# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we
# suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and
# cleared your head.


# Paste your code into this box


def longest_sub(s):
    new_list = []
    long = ""
    i = 0
    j = 0
    while (i < len(s)-1):
        if len(long) == 0:
            long = long + s[i]
        else:
            if (long[j] <= s[i+1]):   # if the previous element is smaller 
                long = long + s[i+1]     # add it to the long string
                j = j + 1
                i = i + 1
            else:
                new_list.append(long)  
                long = ""
                j = 0
                i = i + 1
    
    new_list.append(long)
    return max(new_list, key = len)

print("Longest substring in alphabetical order is :")
print(longest_sub(s))
