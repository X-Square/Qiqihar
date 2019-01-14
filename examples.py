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

# Define 3-variable AND, OR
AND3 = Circuit("111")
OR3 = Circuit("100+010+001+011+101+110+111")
print(AND3("011")) # 0
print(OR3("010")) # 1

# Define 3-variable majority function
MAJ3 = Circuit("110+011+101+111")
print(MAJ3("001")) # 0
print(MAJ3("000")) # 0
print(MAJ3("101")) # 1

# Define 3-variable odd parity function
ODD3 = Circuit("010+100+001+111")
print(ODD3("011")) # 0
print(ODD3("010")) # 1