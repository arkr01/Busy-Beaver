# -*- coding: utf-8 -*-
"""
Test script for running a Turing machine unary adder

Created on Fri Mar 29 21:57:42 2019

@author: shakes
"""
from turing_machine import TuringMachine

# Create the Turing machine
adder = TuringMachine( 
    {
        ('q0', '1'): ('Find0', '1', 'R'),
        ('Find0', '1'): ('Find0', '1', 'R'),
        ('Find0', '0'): ('qa', '', 'R'),
    }
)

print("2+3 Computation")
adder.debug('110111')
print("\n3+4 Computation")
adder.debug('11101111')
