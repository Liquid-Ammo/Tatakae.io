# modules
from subprocess import call  # for clear
import os  # for clear
from time import sleep  # for time delay
from Attack import attack, defence ,  filler , Moves
print(attack)
# to clear the screen
def clear():
    _ = call("clear" if os.name == "posix" else "cls")
    

clear()



p1_hp = 1000
p2_hp = 1000
p1_ck = 1500
p2_ck = 1500

# 6 by 10 matrix for the game back bone

a=[ [" ", 0, 0, 0, 0, 0, 0, 0, 0, " "],
    [" ", 0, 0, 0, 0, 0, 0, 0, 0, " "], 
    [" ", 0, 0, 0, 0, 0, 0, 0, 0, " "],
    [" ", 0, 0, 0, 0, 0, 0, 0, 0, " "], 
    [" ", 0, 0, 0, 0, 0, 0, 0, 0, " "],
    ["O", 0, 0, 0, 0, 0, 0, 0, 0, "O"], 
    ["|", 0, 0, 0, 0, 0, 0, 0, 0, "|"], 
    ["|", 0, 0, 0, 0, 0, 0, 0, 0, "|"],  
    ["^", 0, 0, 0, 0, 0, 0, 0, 0, "^"]]



def printer(c=1):
    clear()
    for i in a:
        if c==1:
            c+=1
            continue
        print(i)
    print()
printer()


def p2i(c):
    if c==1:
        n=0
    elif c==2:
        n=9
    return n

def jump(c=1):
    n=p2i(c)
    
    if a[5][n]=="O":
        #up
        for j in range (2): 
            sleep(0.1)
            for i in range (1,9,1):
                a[i-1][n]=a[i][n]
                if i ==8:
                    a[8][n]=a[0][n]
            printer()    
            
        #down
        for j in range (2): 
            sleep(0.1)
            for i in range (8,-1,-1):
                if i ==8:
                    a[0][n]=a[8][n]
                else:
                    a[i+1][n]= a[i][n]
                printer()
            printer()
    else:
        pass

def duck (c=1):
    n=p2i(c)
    
    #down
    if a[5][n]=="O":
        a[0][n]=a[6][n]
        a[6][n]=a[5][n]
        a[5][n]=a[2][n]
        printer()
        sleep(0.3)
    if a[6][n]=="O":
        a[5][n]=a[6][n]
        a[6][n]=a[0][n]
        a[0][n]=a[1][n]
        printer()
    
def move(x,y):
    if x in attack:
        attacks(x,y)
    elif x in defence:
        defence(x,y)
    elif x in filler:
        filler(x,y)
    else:
        print("Attack type error")
    return a


def attacks(x,y):
    n = p2i(y)
    for i in range (len(a)):
        if a[i][n]=="|":
            for j in range(1,9,1):
                a[i][j]=3
                sleep(0.05)
                printer()
                a[i][j]=0  
            break



for i in range (2):
    ae=int(input("jump"))
    jump(ae)
    be=int(input("duck"))
    duck(be)
    ce=int(input("attack"))
    move("Eye Gouge",ce)