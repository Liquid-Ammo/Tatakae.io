# modules
import pygame
from subprocess import call  # for clear
import os  # for clear
from time import sleep  # for time delay
from Attack import attack, defence ,  filler , Moves

# to clear the screen
def clear():
  _ = call("clear" if os.name == "posix" else "cls")


clear()



p1_hp = 1000
p2_hp = 1000
p1_ck = 1500
p2_ck = 1500

# 6 by 10 matrix for the game back bone
a0 = [" ", 0, 0, 0, 0, 0, 0, 0, 0, " "]
a1 = [" ", 0, 0, 0, 0, 0, 0, 0, 0, " "]
a2 = [" ", 0, 0, 0, 0, 0, 0, 0, 0, " "]
a3 = ["O", 0, 0, 0, 0, 0, 0, 0, 0, "O"]
a4 = ["|", 0, 0, 0, 0, 0, 0, 0, 0, "|"]
a5 = ["|", 0, 0, 0, 0, 0, 0, 0, 0, "|"]
a6 = ["^", 0, 0, 0, 0, 0, 0, 0, 0, "^"] 
print(a0, a1, a2, a3, a4, a5, a6, sep="\n")

# functions


# jumping
def jump(c=1):
    n = 10
    if c == 1:
        n = 0
    if c == 2:
        n = 9
    sleep(0.3)
    clear()
    for i in range(2):
        print(a0, a1, a2, a3, a4, a5, a6, sep="\n")
        a1[n] = a2[n]
        a2[n] = a3[n]
        a3[n] = a4[n]
        a4[n] = a5[n]
        a5[n] = a6[n]
        a6[n] = a0[n]
        sleep(0.1)
        print()
        clear()
    for i in range(2):
        print(a0, a1, a2, a3, a4, a5, a6, sep="\n")
        a6[n] = a5[n]
        a5[n] = a4[n]
        a4[n] = a3[n]
        a3[n] = a2[n]
        a2[n] = a1[n]
        a1[n] = a0[n]
        sleep(0.1)
        print()
        clear()
    print(a0, a1, a2, a3, a4, a5, a6, sep="\n")


# ducking
def duck(c):
    n = 4
    if c == 1:
        n = 0
    if c == 2:
        n = 9
    sleep(0.3)
    clear()
    if True:
        print(a0, a1, a2, a3, a4, a5, a6, sep="\n")
        a0[n] = a4[n]
        a4[n] = a3[n]
        a3[n] = a2[n]
        sleep(0.25)
        print()
        clear()
    if True:
        print(a0, a1, a2, a3, a4, a5, a6, sep="\n")
        a3[n] = a4[n]
        a4[n] = a0[n]
        a0[n] = a1[n]
        sleep(0.25)
        print()
        clear()
    print(a0, a1, a2, a3, a4, a5, a6, sep="\n")

def move_classification(x):
    if x in attack:
        a = 1
    elif x in defence:
        a = 2
    elif x in filler:
        a = 3
    else:
        print("Attack type error")
    return a

def move(x,y):
    a=move_classification(x)
    if a==1:
        attack(x,y)

def attack(x,c):
    n = 10
    if c == 1:
        n = 0
    if c == 2:
        n = 9
    
    if a1[n] == "|":
        for i in range (2,9):
            pass
  

# inputs for now will be part of pygame later
for i in range(0, 4):
    a = int(input("Jump : "))
    jump(a)
    b = int(input("Duck : "))
    duck(b)
    c = tuple(input("Move : "))
    move(c)
