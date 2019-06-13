# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:00:54 2019

@author: Zigma
"""


import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'user_name.json'
    try:
        with open(filename) as f_obj:
            user_name = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return user_name


def get_new_username():
    """Prompt for a new username."""
    user_name = input("What is your name? ")
    filename = 'user_name.json'
    with open(filename, 'w') as f_obj:
        json.dump(user_name, f_obj)
    return user_name


def greet_user():
    """Greet the user by name."""
    user_name = get_stored_username()
    w_back = input(("is " + user_name.title() + " your username? [yes/no]: "))
    if w_back == 'yes':
        print("Welcome back, " + user_name + "!")
    elif w_back == 'no':
        user_name = get_new_username()
        print("We'll remember you when you come back, " + user_name + "!")


greet_user()
