from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtCore
import random

#global variables and values

board = {   #vaslues on the board
    "1":[],
    "2":[],
    "3":[],
    "4":[],
    "5":[],
    "6":[],
    "7":[],
    "8":[],
    "9":[],
    "cells":[],
    "score":[],
    "logo":[],
    "button":[],
    "turn":["X"],
    "winner":[],
    "tie":[]
}

grid = QGridLayout()   #grid on the board
def start_game():
    print('game started')
#create a buttoon

def create_button(l_margin,r_margin):
    button = QPushButton()
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(250)

    button.setStyleSheet(
        #setting variable margins
        "*{margin-left: " + str(l_margin) +"px;"+
        "margin-right: " + str(r_margin) +"px;"+
        '''
        border: 4px solid '#9E3A14';
        color: white;
        font-family: 'shanti';
        font-size: 16px;
        border-radius: 0px;
        padding: 15px 0;
        margin-top: 20px;
        }
        *:hover{
            background: '#E66912';
        }
        '''
    )
    button.clicked.connect(lambda x: next_Turn(button))
    return button
#clear a button/widgets
def clear_board():
    for mark in board:
        if board[mark] != []:
            for i in range(0,len(board[mark])):
                board[mark].pop()
def next_Turn(btn):
    player = btn.text()
    if player == "":
        if board["turn"][-1] == "X":
            X_mark(btn)
        else:
            O_mark(btn)
        #if tie_check():
         #   print('The game Ended in a tie')
        #else:
         #   print(board["winner"][-1]+ " Player Won the game")

#add X marker
def cell_name(name):
    return name
def X_mark(button):
    button.setText('X')
   # O_mark(button)
    board["turn"].pop()
    board["turn"].append("Y")

#add O Marker
def O_mark(button):
    button.setText('Y')
    board["turn"].pop()
    board["turn"].append("X")

#check rows
def row_check():
    cells = board["cells"]
    print(type(cells))
    print('***********')
    for i in range(0,3):
        m = i*3
        print(cells[0+m])
        print('****')
        if cells[0+m] == cells[1+m] == cells[2+m] != "":
            return True


#check columns
def columns_check():
    cells = board["cells"]
    for i in range(0,3):
        if cells[i] == cells[i+3] == cells[i+6] != "":
            return True
#check diagnals
def diagnal_check():
    cells = board["cells"]
    if cells[0]==cells[4]==cells[8] != "":
        return True
    if cells[2] == cells[4] == cells[6] != "":
        return True
    else:
        return False
# check winner N/A
def win_check():
    if row_check() == True:
        frame4()
    if columns_check() == True:
        frame4()
    if diagnal_check() == True:
        frame4()
# check tie
def tie_check():
    if row_check() == columns_check() == diagnal_check() != True:
        return True
    else:
        board["winner"].append(board["turn"][-1])
        return False
#check score best 2 out of 3

#frame 1 >>> decide whether the game will be single player or multi player
def frame1():
    #intro logo page
    clear_board()
    image = QPixmap('banner.png')
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    board["logo"].append(logo)

    #play button
    button = QPushButton("Play")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        '''
        *{
            border: 4px solid '#E66912';
            border-radius: 45px;
            font-size: 35px;
            color: 'white';
            padding: 25px 0;
            margin: 100px 200px;
        }
        *:hover{
            background: '#E66912';
        }
        '''
    )
    board["button"].append(button)

    grid.addWidget(board["logo"][-1],0,0,1,2)
    grid.addWidget(board["button"][-1],1,0,1,2)

#frame 2 >>> Game, score is how many games won
def frame2():

    image = QPixmap('banner1.png')
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    board["logo"].append(logo)

    button1 = create_button( 100, 1)
    button2 = create_button( 50, 50)
    button3 = create_button( 1, 100)

    button4 = create_button(100, 1)
    button5 = create_button(50, 50)
    button6 = create_button(1, 100)

    button7 = create_button(100, 1)
    button8 = create_button(50, 50)
    button9 = create_button(1, 100)

    clicker = [button1,button2,button3,button4,button5,button6,button7,button8,button9]
    board["cells"].append(clicker)

    grid.addWidget(board["logo"][-1], 0, 0, 1, 3)

    grid.addWidget(button1,1,0)

    grid.addWidget(button2,1,1)
    grid.addWidget(button3,1,2)

    grid.addWidget(button4, 2, 0)
    grid.addWidget(button5, 2, 1)
    grid.addWidget(button6, 2, 2)

    grid.addWidget(button7, 3, 0)
    grid.addWidget(button8, 3, 1)
    grid.addWidget(button9, 3, 2)
    i = 0
    #for column in c:
        # for row in c:
          #  board["r" + c[row] + "c" + c[column]].append(clicker[i])
           # i = i + 1
            #print(i)

#frame 3 >>> Lost the game window and a try again
def frame3():
    print("frame3")

#frame 4 >>> Won the game play again
def frame4():
    print("frame4")