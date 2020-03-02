# -*- coding: utf-8 -*-
"""
__author__ = ""Zack Khalidov"
__email__ = 'zakhaddin1995@gmail.com'
__version__ = '0.1'

This program simulates a die.
"""
import random

min = 1
max = 6

def dice_roll():
        return random.randint(min, max)

def print_die():
        print("die:", dice_roll())

def looper():

        print("Press any key to roll (space to quit)")
        try:
            key = input(">")
        except:
            print("Invalid character error")
        #loops until space is entered
        while key != " ":
            print_die() #calls printer method
            try:
                key = input(">")
            except:
                print("Invalid character error")

        print("Bye!")

if '__main__' == __name__:
    looper()
