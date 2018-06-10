#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 5 14:57:46 2017

@author: Ujjwal
"""

import math
def polysum(n,s):
    area = (0.25 * n * s ** 2)/math.tan(math.pi/n)
    perim = n * s
    total =  area + perim
    return round(total, 4)
