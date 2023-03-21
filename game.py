# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 20:12:27 2023

@author: Mohammed Adnan khan
"""

from chapter1 import chapter1
from chapter2 import chapter2
from chapter3 import chapter3
from chapter4 import chapter4
from chapter5 import chapter5
def run():
    res = chapter1()
    # print("Res %d" % res) # for debugging chapters' return values
    if res == 2:
        
        res = chapter2()
    if res == 1:
        run()
        return
    if res == 3:
        print("c3")
        res = chapter3()
    # print("res: ", res)
    if res == 1:
        run()
    elif res == 4:
        res = chapter4()
    # print("res: ", res)
    if res ==1:
        run()
    elif res == 5:
        res = chapter5()
    if res == 1:
        run()
    
    
    
if __name__ == "__main__":
    run()
    