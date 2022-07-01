# -*- coding: utf-8 -*-
"""
2 State Busy Beaver
"""
from turing_machine import TuringMachine


# Create the Turing machine
bbeaver = TuringMachine( 
    { 
        ('a', '0'): ('b', '1', 'R'),
        ('a', '1'): ('b', '1', 'L'),
        ('b', '0'): ('a', '1', 'L'),
        ('b', '1'): ('h', '1', 'R')
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)

bbeaver.debug('00000000000000', step_limit=1000)
