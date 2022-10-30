import os

n = 1
dict = {"a1": " ", "a2": " ", "a3": " ", "b1": " ", "b2": " ", "b3": " ", "c1": " ", "c2": " ", "c3": " "}
true_values = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
session = True

def winner():
    if dict['a1'] == "X" and dict['a2']== "X" and dict['a3']== "X" or dict['a1'] == "X" and dict['b1']== "X" and dict['c1']== "X" or dict['a2'] == "X" and dict['b2']== "X" and dict['c2']== "X" or dict['a3'] == "X" and dict['b3']== "X" and dict['c3']== "X" or dict['b1'] == "X" and dict['b2']== "X" and dict['b3']== "X" or dict['c1'] == "X" and dict['c2']== "X" and dict['c3']== "X" or dict['a1'] == "X" and dict['b2']== "X" and dict['c3']== "X" or dict['a3'] == "X" and dict['b2']== "X" and dict['c1']== "X":
        os.system('cls')
        print("PLAYER 1 WIN")
        play_again = input("Play again?")
        if play_again == 0:
            session = False
        else:
            dict.fromkeys(dict," ")
            
        os.system('cls')
    if dict['a1'] == "O" and dict['a2']== "O" and dict['a3']== "O" or dict['a1'] == "O" and dict['b1']== "O" and dict['c1']== "O" or dict['a2'] == "O" and dict['b2']== "O" and dict['c2']== "O" or dict['a3'] == "O" and dict['b3']== "O" and dict['c3']== "O" or dict['b1'] == "O" and dict['b2']== "O" and dict['b3']== "O" or dict['c1'] == "O" and dict['c2']== "O" and dict['c3']== "O" or dict['a1'] == "O" and dict['b2']== "O" and dict['c3']== "O" or dict['a3'] == "O" and dict['b2']== "O" and dict['c1']== "O":
        os.system('cls')
        print("PLAYER 2 WIN ")
        play_again = input("Play again? ")
        if play_again == 0:
            session = False
        else:
            dict[::1] = " "
        os.system('cls')
    if n>=9:
        os.system('cls')
        print("DRAW")
        play_again = input("Play again? ")
        if play_again == 0:
            session = False
        os.system('cls')
while session:
    os.system('cls')
    enter = True
    winner()
    print(f""" 
             A   B   C
          1  {dict['a1']}   {dict['b1']}   {dict['c1']}
          2  {dict['a2']}   {dict['b2']}   {dict['c2']}
          3  {dict['a3']}   {dict['b3']}   {dict['c3']}
          """)
    
    while enter:
        if n%2!=0:
            step = input("PLayer 1: ")
            if dict.get(step)==" " and step in true_values:
                dict[step] = "X"
                enter = False 
            else:
                print("Wrong value") 
        else: 
            step = input("PLayer 2: ")
            if dict.get(step)==" " and step in true_values:
                dict[step] = "O"
                enter = False 
            else:
                print("Wrong value") 
    n+=1

