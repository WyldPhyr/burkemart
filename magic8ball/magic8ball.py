# -*- coding: utf-8 -*-
"""
@author: WyldPhyr
"""

from random import randint

def rand():
    num = randint(0, 9)
    run(num)

def run(num):
#   This is to prevent the rest of the program from running until the user asks
#   a question. Plus there's a super secret Easter egg!
    question = raw_input("What is your yes or no question? ")

#   Easter egg (super secret)
    if question in ["password123"]:
        print("Happy Easter!")
    else:
        print(" ")
    
    if num == 0:
        print("Yes, and you will be happy!")
    elif num == 1:
        print("No, and if you try, it will not end well.")
    elif num == 2:
        print("Yes.")
    elif num == 3:
        print("No.")
    elif num == 4:
        print("Maybe so.")
    elif num == 5:
        print("Perhaps.")
    elif num == 6:
        print("Without a doubt.")
    elif num == 7:
        print("Only on Sundays.")
    elif num == 8:
        print("Ask again later.")
    elif num == 9:
        print("42.")
    else:
#       Yay for error messages!
        print("Sorry, the future is cloudy today. Please restart and try again.")

while True:
    run(num)
    rep = raw_input("Would you like to ask another question? ")
    if rep in ["Yes", "yes", "y", "Y"]:
        print("Okay.")
    else:
        break