# -*- coding: utf-8 -*-
"""
Busy beaver Turing machine with 4 states.

Created on Tue Apr 13 21:04:25 2021

@author: arajka
"""
from turing_machine import TuringMachine

# Create the Turing machine
bbeaver = TuringMachine(
    {
        ('a', '0'): ('b', '1', 'L'),
        ('a', '1'): ('d', '1', 'L'),
        ('b', '0'): ('d', '1', 'R'),
        ('b', '1'): ('h', '1', 'L'),
        ('c', '0'): ('a', '1', 'R'),
        ('c', '1'): ('d', '0', 'R'),
        ('d', '0'): ('c', '1', 'R'),
        ('d', '1'): ('b', '1', 'R')
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)

bbeaver.debug('00000000000000', step_limit=1000)
