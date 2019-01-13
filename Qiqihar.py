#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 12:19:29 2019

@author: X-Square
"""

class Circuit:
    'The Boolean Circuit Base Class'
    
    def __init__(self, numInput, exprR):
        self.numInput = numInput
        self.exprR = exprR
    
    def __processExpr(self):
        self.exprP = self.exprR.split('+')
    
    def __call__(self, boolInput):
        return self.out(boolInput)
        
    def out(self, boolInput):
        self.__processExpr()
        for item in self.exprP:
            if boolInput == item:
                return "1"
        return "0"

AND = Circuit(2,"11")
OR = Circuit(2,"10+01+11")
NOT = Circuit(1,"0")

# t1 = Circuit(NOT(AND(AND()+OR())))
def t1(intext):
    return NOT(OR(AND(intext[0:2])+OR(intext[2:4])))