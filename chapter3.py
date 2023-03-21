# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:26:57 2023

@author: Mohammed Adnan khan
"""
import random

intro = "Welcome to chapter 3"
def talk_to_witness():
    statements = ["I saw a suspect breaking into the house but the suspect was wearing a mask.",
                  "On one hand there was a gun probably a glock.",
                  "There was some quick noise of the glass breaking at the door",
                  "It all happened so fast.",
                  "I was scared and hid behind a car"
                  ]
    
    names = ["Annabelle", "Rosaline", "Mike Olson", "Juan Xhin", "Ho Lee Chan"]
    name = random.choice(names)
    print("Hi! I'm %s" %name)
    talks = []
    for x in range(len(statements)):
        s = random.choice(statements)
        if s not in talks:
            talks.append(s)
    
    if len(talks) >3: talks = talks[:3]
    random.shuffle(talks)
    for x in talks:
        print("%s" % x)
    

def interrogate():
    info = ["No I was at home.", 
            "I was watching TV alone",
            "No I only talked to my friend via whatsapp"]
    qs = ["Where were you on that day?",
          "Do you have an allaby?",
          "Your gps signal shows otherwise"]
    
    for x in range(len(qs)):
        print(f"Me: {qs[x]}")
        print(f"Suspect: {info[x]}")
    else:
        print("Thank you for your cooperation!")
def follow_leads():
    # chapter4()
    return 4

def start_chapter1():
    # chapter1()
    return 1
def action():
    print("Select an action...")
    print("1. Interrogate")
    print("2. Follow leads")
    print("3. Go back to the hotel")
    try:
        choice = int(input(">>"))
        if choice <1 or choice >3:
            raise Exception("Invalid choice")
        if choice == 1:
            interrogate()
        elif choice == 2:
            return follow_leads()
        elif choice == 3:
            return start_chapter1()
        return action()
    except Exception as ex:
        print("Error! %s" %ex)
def chapter3():
    global intro
    print(intro)
    talk_to_witness()
    return action()
    