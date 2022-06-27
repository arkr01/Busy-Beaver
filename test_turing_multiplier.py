# -*- coding: utf-8 -*-
"""
Test script for running a Turing machine unary adder

Created on Fri Mar 29 21:57:42 2019

@author: shakes
"""
from turing_machine import TuringMachine

# Create the Turing machine
multiplier = TuringMachine(
    {
        ('q0', '1'): ('FindRightMost', '1', 'R'),
        ('FindRightMost', '1'): ('FindRightMost', '1', 'R'),
        ('FindRightMost', '0'): ('FindRightMost', '0', 'R'),
        ('FindRightMost', ''): ('FindNext1', '0', 'L'),

        ('FindNext1', '1'): ('FindNext1', '1', 'L'),
        ('FindNext1', '0'): ('FindNext1', '0', 'L'),
        ('FindNext1', ''): ('FoundNext1', '', 'R'),
        ('FindNext1', 'X'): ('FoundNext1', 'X', 'R'),

        ('FoundNext1', '1'): ('FindMultiples', 'X', 'R'),
        ('FindMultiples', '1'): ('FindMultiples', '1', 'R'),
        ('FindMultiples', '0'): ('CheckLastX', '0', 'L'),

        ('CheckLastX', 'X'): ('CheckLastX', 'X', 'R'),
        ('CheckLastX', '0'): ('StartMultiplying', 'A', 'R'),
        ('CheckLastX', '1'): ('GoToStartMultiply', '1', 'R'),

        ('GoToStartMultiply', '1'): ('GoToStartMultiply', '1', 'R'),
        ('GoToStartMultiply', '0'): ('StartMultiplying', '0', 'R'),

        ('StartMultiplying', '1'): ('WriteAnswer', 'Y', 'R'),
        ('WriteAnswer', '1'): ('WriteAnswer', '1', 'R'),
        ('WriteAnswer', '0'): ('CheckLastY', '0', 'L'),

        ('CheckLastY', 'Y'): ('CheckLastY', 'Y', 'R'),
        ('CheckLastY', '0'): ('WriteAnswer', 'B', 'R'),
        ('CheckLastY', '1'): ('GoToMultiply', '1', 'R'),

        ('GoToMultiply', '1'): ('GoToMultiply', '1', 'R'),
        ('GoToMultiply', '0'): ('WriteAnswer', '0', 'R'),

        ('WriteAnswer', ''): ('BackToQuestion', '1', 'L'),

        ('BackToQuestion', '0'): ('BackToQuestion', '0', 'L'),
        ('BackToQuestion', '1'): ('BackToQuestion', '1', 'L'),
        ('BackToQuestion', 'Y'): ('StartMultiplying', 'Y', 'R'),
        ('BackToQuestion', 'B'): ('NextDigit', '0', 'L'),

        ('NextDigit', 'Y'): ('NextDigit', '1', 'L'),
        ('NextDigit', '0'): ('NextDigit', '0', 'L'),
        ('NextDigit', '1'): ('NextDigit', '1', 'L'),
        ('NextDigit', 'X'): ('FoundNext1', 'X', 'R'),
        ('NextDigit', 'A'): ('End', '0', 'L'),

        ('End', 'X'): ('End', '1', 'L'),
        ('End', ''): ('qa', '', 'R')
    }
)

print("2*4 Computation")
multiplier.debug('101', step_limit=1000)
# print("\n2*3 Computation")
# multiplier.debug('110111', step_limit=1000)
# print("\n3*5 Computation")
# multiplier.debug('111011111', step_limit=1000)
