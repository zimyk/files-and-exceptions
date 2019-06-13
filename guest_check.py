# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 12:23:06 2019

@author: Zigma
"""


filename = 'prog_poll.txt'

with open(filename) as file_object:
    lines = file_object.read()
    print(lines.strip())
