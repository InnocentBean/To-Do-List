#For Convenience Purposes
import time as t
import os as o


#Kinda need this list, and The num Var Too
todo = ["Filler Text","Filler Text"]
num = 1


#Core Piece, Brings Everything Together
def do():
    o.system('cls')
    global num, todo
    t.sleep(0.5)
    print("This is your To-Do list:")
    num = 1
    for i in todo:
        print(str(num)+": "+i)
        num+=1
    num =1
    t.sleep(0.5)
    print("Choose one thing to do.\nChange\t1\nAdd\t2\nRemove\t3")
    inp=input("")
    if inp == "1":
        change()
    elif inp =="2":
        add()
    elif inp =="3":
        remove()
    else:
        do()


#Changes Pre-Existing List Stuff
def change():
    global todo, num
    o.system('cls')
    t.sleep(0.5)
    print("This is your To-Do list:")
    for i in todo:
        print(str(num)+": "+i)
        num+=1
    print("What number would you like to change?")
    inp = input("")
    todo[int(inp)-1] = input("What would you like it to be instead?\n")
    do()


#Adds Things To To-Do List
def add():
    global todo, num
    o.system('cls')
    t.sleep(0.5)
    print("What would you like to add?")
    inp = input()
    todo.append(inp)
    do()


#Removes Things From To-Do List
def remove():
    global todo, num
    t.sleep(0.5)
    print("Which item would you like to remove?")
    inp=input()
    print("Type the exact text to confirm: ")
    inp = input()
    todo.remove(inp)
    do()


#Starts The Madness
do()