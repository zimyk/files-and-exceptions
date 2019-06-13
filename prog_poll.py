# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 07:27:43 2019

@author: Zigma
"""


polls = []
prompt = "Hit the spacebar + enter to exit\n"
prompt += "Can you spare us a minute of your time?\n"
prompt += "Why do you like Programmimg? "
while True:
    poll = input(prompt)
    if poll == " ":
        break
    polls.append(poll)

filename = "prog_poll.txt"
with open(filename, "w") as f_obj:
    for poll in polls:
        f_obj.write(poll + "\n")
