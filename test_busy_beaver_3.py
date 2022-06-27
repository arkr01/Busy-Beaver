# -*- coding: utf-8 -*-
"""
Busy beaver Turing machine with 3 states.

Created on Tue Apr 13 13:55:25 2021

@author: arajka
"""
from turing_machine import TuringMachine

# Create the Turing machine
bbeaver = TuringMachine(
    {
        ('a', '0'): ('b', '1', 'R'),
        ('a', '1'): ('c', '1', 'L'),
        ('b', '0'): ('a', '1', 'L'),
        ('b', '1'): ('c', '1', 'R'),
        ('c', '0'): ('b', '1', 'L'),
        ('c', '1'): ('h', '1', 'R')
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)

bbeaver.debug('00000000000000', step_limit=1000)
