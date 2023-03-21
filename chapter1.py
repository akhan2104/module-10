# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:45:21 2023

@author: Mohammed Adnan khan
"""
import random
def investigate_crime():
    print("Crime scene")
    l = ["broken window on the left side of the door",
         "cracked Smart TV",
         "white sheet with some blurr shoe marks",
         "fingure prints on the top drawer under the blue light"]
    #shuffle list
    random.shuffle(l)
    print("You make the following observations")
    data = []
    for x in range(3):
        print(f"\ta {l[x]} ")
        data.append(f"a {l[x]}")
    return data
    
    
def search_suspect():
    print("Search for suspects")
    # go to chapter 2
    return 2

def interact_police(l):
    print("Interact with police")
    print("Hello DCI officer! What's your name")
    names = ['Mark', 'Annette', 'Julius', 'Annabelle', 'Khalid', 'Khalifa']
    random.shuffle(names)
    name = random.choice(names)
    print("Officer: I am %s" % name)
    if l is not None and len(l) !=0:
        print("Hello %s! I have collected the following information this far..." %name)
        for x in l:
            print(f"{x}")
        print("%s: Thank you so much for this information, we will investigate the crime with our forensics team" % name)
    else:
        print("Hello %s! I have not collected any information" % name)
        print("%s: Thank you for reaching out, please feel free to reach out to us in case of any new information" %s)

def rest(how_long:int):
    print("resting for %d minutes" %how_long)
def action(observations:list = []):
    print("You are now in the city")
    print("-----choose an action----")
    print("1. Search for clues")
    print("2. Search for suspect")
    print("3. Interact with police")
    print("4. Stay")
    print("0. Quit")
    try:
        choice = int(input(">>"))
        if choice <0 or choice >4:
            raise Exception("Invalid choice")
        if choice == 1:
            observations = investigate_crime()
        elif choice == 2:
            return search_suspect()
        elif choice == 3:
            interact_police(observations)
        elif choice == 4:
            how_long = int(input("Enter how long you wish to stay in hotel in minutes: "))
            rest(how_long)
        elif choice == 0:
            print("Quiting game!")
            return 0
        return action(observations)
    except Exception as ex:
        print("Please choose an action! %s" % ex)
def chapter1():
    intro = "Welcome to chapter 1"
    print(intro)
    return action()
    
if __name__=="__main__":
    chapter1()