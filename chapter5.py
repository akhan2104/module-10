# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 19:54:58 2023

@author: Mohammed Adnan khan
"""


from chapter4 import search_warehouse
import random
def confront_figure():
    print("Confronting mysterious figure")
    print("Hello, I am Alice Belle a police officer. What's your nname?")
    names = ['Ian', 'James', 'Mark', 'Lucy', 'Anna', 'Mia', 'Khalid']
    fig = random.choice(names)
    print("I am %s. How can I help you?" % fig)
    print("Me: I would like your assistance on an investigation")
    print("%s: Sure I can help you with that information" % fig)
    print("Me: Thank you so much %s" %fig)
    return fig
def search_room():
    print("Searching for a room")
    search_warehouse()

def talk(name:str):
    info = ["I was in the shower. ",
            "I heard a loud noise and moved to the window.",
            "I saw a man breaking into the house",
            "Since I was at the 5th floor I was able to see the man unmasking himself",
            "He had a dragon tatoo at the back of the head.",
            "He was white probably from Mexico due to the color compression."
            "About 6.5 inch tall"]
    random.shuffle(info)
    print("Me: What happened %s" %name)
    print("%s: " % name)
    for inf in info:
        print(f"{name}: {inf}")
    
def action(name:str= None):
    print("Select an action...")
    print("1. Search for a room")
    print("2. Talk to figure")
    print("3. Confront figure")
    print("4. Go back to hotel")
    try:
        choice = int(input(">>"))
        if choice <1 or choice >4:
            raise Exception("Invalid choice!")
        if choice == 1:
            search_room()
        elif choice == 2:
            talk(name)
        elif choice == 3:
            name = confront_figure()
        elif choice ==4:
            return 1
        return action(name)
    except Exception as ex:
        print("Error! %s" %ex)
        return action(name) # continue 
def chapter5():
    print("Welcome to chapter 5")
    confront_figure()
    return action()