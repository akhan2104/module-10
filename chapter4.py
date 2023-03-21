# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:32:52 2023

@author: Mohammed Adnan khan
"""
import random

items = ['broken glass', 'knife', 'radio with blood', 'fingure prints under blue light']
warehouses = {f"warehouse {x+1}": [random.choice(items) for i in range(4)] for x in range(5)}
def search_warehouse():
    print("Search the warehouse...")
    
    choice = input("Enter warehouse number: ")
    if f'warehouse {choice}' in warehouses:
        w = warehouses[f'warehouse {choice}']
        for i in w:
            print(i)

def show_journal():
    journals = ["The Return of Spiderman", "Death on A Desert", "American Crime History", "The 3 Musketeers"]
    print(f"Here is a journal for you! '{random.choice(journals)}'")
def action():
    print("\nSelect an action...")
    print("1. Look for clues")
    print("2. Open the door")
    print("3. Go back to hotel")
    try:
        choice = int(input(">>"))
        if choice <1 or choice > 3:
            raise Exception("Invalid choice!")
        if choice == 1:
            show_journal()
        elif choice == 2:
            return 5
        elif choice == 3:
            return 1
        return action()
    except Exception as ex:
        print("Error! %s" %ex)
    
def chapter4():
    print("Welcome to chapter 4")
    return action()