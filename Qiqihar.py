#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 12:19:29 2019

@author: X-Square
"""

class Circuit:
    'The Boolean Circuit Base Class.'
    
    def __init__(self, expr):
        if type(expr) == str:
            self.ruleR = expr
            self.type = 1
        else:
            self.func = expr
            self.type = 2
    
    def __processRule(self):
        self.ruleP = self.ruleR.split('+')
    
    def __call__(self, boolInput):
        if self.type == 1:
            return self.__out(boolInput)
        else:
            return self.func(boolInput)

    def __out(self, boolInput):
        self.__processRule()
        for item in self.ruleP:
            if boolInput == item:
                return "1"
        return "0"

# Common gates
AND = Circuit("11")
OR = Circuit("10+01+11")
NOT = Circuit("0")

# Useful gates
XOR = Circuit("01+10")
NOR = Circuit(lambda intext: NOT(OR(intext)))
NAND = Circuit(lambda intext: NOT(AND(intext)))