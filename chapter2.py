# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 16:42:12 2023

@author: Mohammed Adnan khan
"""
import random
# from chapter1 import chapter1
# from chapter3 import chapter3
intro = "Welcome to chapter 2"

houses = ['house%d' % x for x in range(1, 5)]
houses = {house: random.randint(1, 10) for house in houses}
items = ['clock', 'mouse', None]
basements = {house: random.choice(items) for house in houses}
collections = []
def search_house():
    global houses
    print("Search for a house...")
    for k in houses:
        print("House: %s" %k)
    choice = input("Enter the house to search for: ")
    if choice in houses:
        house = houses[choice]
        print("You have selected house: %s" %choice)
        return choice
    return None

def findKey(house:str):
    global houses
    print("Look for keys...", house)
    
    if house in houses:
        print(f"Key for {house} is %s" % houses[house])
    else:
        print("house %s not found in houses" %house)
        

def search_basement(house):
    global houses, basements, collections
    print("Search basement...")
    
    if house in houses:
        # show the items in basement
        item = basements[house]
        if item is not None:
            print("This basement contains a %s" % item)
            choiceyn = input("Take item? (y/n)")
            choiceyn = choiceyn.lower()
            if choiceyn == 'y':
                print("You have taken the %s" % item)
                collections.append("Item:%s" % item)
                basements[house] = None
                print("You have now collected the followig items")
                for c in collections:
                    print(c, end=", ")
                print()#new line
            
        else:
            print("Basement has no item(s)")



def talk_to_witness():
    # chapter3()
    return 3
            
def chapter2():
    global intro
    print(intro)
    return action()

def action():
    house = search_house()
    
    print("Select an action.....")
    print("1. Look for keys")
    print("2. Talk to witness")
    print("3. Search basement")
    print("4. Leave house")
    try:
        choice = int(input(">>"))
        if choice <1 or choice >4:
            raise Exception("Invalid choice")
        if choice == 1:
            findKey(house)
        elif choice == 2:
            return talk_to_witness()
        elif choice == 3:
            search_basement(house)
        elif choice == 4:
            print("Leaving the house")
            return 1
        return action()
    except Exception as ex:
        print("Error! %s" %ex)

if __name__=="__main__":
    chapter2()