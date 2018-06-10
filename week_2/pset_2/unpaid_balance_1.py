#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 8 20:48:23 2016

@author: Ujjwal
"""

# Paste your code into this box
# Paste your code into this box
def end_year_balance(balance, interest, monthly_payment):
    
    for i in range(11):
        minimum_payment = balance * monthly_payment/100
        unpaid_balance = balance - minimum_payment
        total_unpaid_balance = unpaid_balance + (interest/(12*100)) * unpaid_balance
        balance = total_unpaid_balance
    
    return round(total_unpaid_balance, 2)

print(end_year_balance(5000, 18, 12))
