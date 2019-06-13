# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:52:03 2019

@author: Zigma
"""


def cats_dogs(filename):
    """ Analyses text documents"""

    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        print(filename + " contains:")
        print(contents)


files = ['cats.txt', 'dogs.txt']
for file in files:
    cats_dogs(file)
