#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 23:43:08 2019

@author: X-Square
"""

from Qiqihar import Circuit, AND, OR, NOT

# Let's create a random Circuit using AND, OR and NOT.
c1 = Circuit(lambda intext: NOT(OR(AND(intext[0:2])+OR(intext[2:4]))))
print(c1("0100")) # 1
print(c1("1001")) # 0

# Let's define a Circuit that always negates c1
c2 = Circuit(lambda intext: NOT(c1(intext)))
print(c2("0100")) # 0
print(c2("1001")) # 1

# Let's define a Circuit that flips 4 bit input
flip4 = Circuit(lambda intext: NOT(intext[0])+NOT(intext[1])+NOT(intext[2])+NOT(intext[3]))
print(flip4("1001")) # 0110
print(flip4("0010")) # 1101