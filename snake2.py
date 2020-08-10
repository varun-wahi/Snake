import os
import random
import time
from msvcrt import getch


### POS_Y =row
### POS_X=column

#######################GLOBAL VARIABLES#######################
time_start=time.time()
pos_x=10
pos_y=10
points=0
arr_board= [[" " for i in range (0,30)]for j in range(0,30)]
size=0
##############################################################
def main():
    print_board()
    pos()
##############################################################

def food():
    global time_start
    time_now=time.time()
    if (time_now-time_start)%10>=0 and (time_now-time_start)%10<=0.5 :
        rand_x=random.randint(1,29)
        rand_y=random.randint(1,29)
        if arr_board[rand_x][rand_y]=="*":
            food()
        else:
            arr_board[rand_x][rand_y]="X"
    elif (time_now-time_start)%15>=0 and (time_now-time_start)%15<=0.5 :
        rand_x=random.randint(1,29)
        rand_y=random.randint(1,29)
        if arr_board[rand_x][rand_y]=="*":
            food()
        else:
            arr_board[rand_x][rand_y]="$"

###############################################################

def print_board():
    global points
    os.system('cls')
    print("-"*25,"S N A K E ","-"*25)
    for k in arr_board:
        print("|",*k,"|")
    print("-"*63)
    print("Points:",points)
    pos()

###################################################################

def pos():
    global arr_board
    global pos_y
    global pos_x
    food()
    user_input=getch().decode("ASCII")
    #user_input=input(";;")
    user_input=user_input.lower()
    if user_input=="w":
        if pos_y==0:##border
            pos_y=29

        pos_y-=1
    elif user_input=="d":
        if pos_x==29:
            pos_x=0

        pos_x+=1
    elif user_input=="s":
        if pos_y==29:
            pos_y=0

        pos_y+=1
    elif user_input=="a":
        if pos_x==0:
            pos_x=29

        pos_x-=1
    elif user_input!="a" or user_input!="s" or user_input!="w" or user_input!="d":
        print("try again!")
        pos()
    death_or_not(pos_y,pos_x)####
    arr_board[pos_y][pos_x]="*"
    print_board()

######################################################################

def death_or_not(pos_y,pos_x):
    global arr_board
    global points
    if arr_board[pos_y][pos_x]=="*":
        print("\n+++++++ D E A D ++++++++")
        print("      Points:",points,"\n Press Enter To Restart")
        #HighScore_write(points)
        points=0
        pos_y=10
        pos_x=0
        arr_board= [[" " for i in range (0,30)]for j in range(0,30)]
        input()
        main()
    else:
        if arr_board[pos_y][pos_x]=="X":
            points+=5
        elif arr_board[pos_y][pos_x]=="$":
            points+=30

########################################################################

def delete(user_input):
    global arr_board
    arr_board[pos_y][pos_x]="*"
    if user_input=="a":
        arr_board[pos_y][pos_x+1]=" "
    elif user_input=="d":
        arr_board[pos_y][pos_x-1]=" "
    elif user_input=="w":
        arr_board[pos_y+1][pos_x]=" "
    elif user_input=="s":
        arr_board[pos_y-1][pos_x]=" "


#########################################################################
def size():
    pass


#########################################################################
def HighScore_write(points):
    scr=open("high.txt",'a+')
    score_list=scr.readline()
    score_list=score_list+str(points)
    score_list=score_list+","
    k=score_list.split(",")
    k.pop()[-1]
    read=[]
    for j in k:
        int(j)
        read.append(j)
    scr.writelines(k)
    scr.close()
    print("High Score:",max(read))

def HighScore_read(score_list):
    k=score_list.split(",")
    k.pop()[-1]
    read=[]
    g=open("high.txt",'r')
    for j in k:
        int(j)
        read.append(j)
    print("High Score:",max(read))
    g.close()


#########################################################################
main()
input()
### POS_Y =row
### POS_X=column
