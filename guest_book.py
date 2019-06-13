# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 06:55:33 2019

@author: Zigma
"""


names = []
prompt = "Hit the space bar twice to exit\n"
prompt += "Please enter your full name: "

while True:
    name = input(prompt)
    print("Hello, " + name.title() + "!")
    if name == "  ":
        break
    names.append(name)

filename = "guest_book.txt"
with open(filename, "w") as f_obj:
    for name in names:
        f_obj.write(name.title() + "\n")
