This is a text based console game that provides the user with a series of chapters in their adventure.
The program contains of 6 files namely:
i) Game.py - This is the game entry point that calls or other modules
ii) Chapter1.py - The first chapter that allows the user to search for clues, suspect, interact with police and stay/rest
iii) Chapter2.py - This is the second chapter that allows the user to [look for keys, talk with witness, search the basement, and leave the house]
iv) Chapter3.py - Third chapter that allows the user to [interrogate suspect, follow leads, and go back to the hotel]
v) Chapter4.py - Fourth chapter that allows the user to [look for clues, open the door, and go back to the house]
vi) and Chapter5.py - Fifth chapter that allows the user to [Search for a room, talk to figure, confront figure, and go back to the hotel] 

A key point to note is that all the 5 chapters consist of a function (action) that takes no parameters but return a value indicating
the next chapter to go to. Also the function is recursive in that only at a break condition does the chapter end, 
for example, on chapter5.py the only break condition that ends the 
recursive action function is choice 4 (which is 'go back to the hotel').
Any of the other choices whether invalid or valid performs an action (or prints the invalid message) and reprints the menu for the user
to select another action to perform.

The action functions are structured in a way that all the choices are handled by helper functions which are called inside the if blocks
To quit the game, the user can input choice 0 at the start of the game since the if blocks do not handle the '0' choice.

Chapters in details...
Chapter1.py
    The investigateCrime() function consists of a list of possible crimes. They can be changed by adding/removing/modifying the list 'l'.
     The list order is changed every time the function is called using the random module
     Moreover, to create some uniqueness on each call, I have limited the number of observations to 3 so that we don't print the whole crime scene at once.
     This function returns a list of information that can be used throughout the chapter

     The interact_police() function takes a list of observations retrieved from the investigateCrime function and creates some interaction with
     a random police officer

     The searchforsuspect function returns the number 2 which is where the next chapter is

Chapter2.py
    It has global variables houses, items, and basements
        The search_house function prints the list of houses by their keys in the dictionary, then asks the user to select a house from the list to search.
        It then returns the housekey value or None if no house found using the user input.
    The search_basement function takes the housekey as an argument and prints the basement items if the key is valid
        This function allows the user to collect items from the basement of the house or print missing values in basement

Chapter3.py
    The talk_to_witness function creates some random interaction with a random witness. CRUD operations can be performed on the statements list and also the names list
    The interrogate function creates some interrogation with the suspect using two lists, where each index in the qs list corresponds to the same index in the info list
    The follow_leads returns chapter 4 ('4'), and the start_chapter1 returns chapter1 (1)

Chapter4.py
    The search_warehouse function takes a warehouse number from user and 
        prints the warehouse details if the number is a key in the warehouses dictionary
    The show_journal function prints a random Journal

Chapter5.py
    The confront_figure function creates a fixed interaction with a random figure/witness 
    The search_room function calls the search_warehouse function from Chapter4
    The talk function prints information from a witness

The coding conventions used are camelCase for variable naming and lower_case for function naming
If a new chapter is added to the game It should consist of a function 'action' that acts as the menu for the chapter, and a function which names the chapter (e.g. chapter7() for chapter 7)
    Finally, the chapter[number] should be imported in the game module and added in the if statements of the game.py

NB: To run the game ensure you have python3 installed eg. python3.8,python3.6 etc.
    Then navigate to the folder where this readme.txt is located using the terminal and type the following command
    python game.py
    or
    python3 game.py #if using conda environment

    Feel free to modify the program as you like (GNU public license)
    


