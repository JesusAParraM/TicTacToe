from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtCore
import random

#global variables and values

board = {   #vaslues on the board
    "cells":["","","","","","","","","",""],
    "score":[],
    "logo":[],
    "button":[],
    "turn":["X"],
    "winner":[],
    "tie":[],
    "logoBottom":[]
}
score_keeper = {
    "winner":[],
    "score":[],

}
grid = QGridLayout()   #grid on the board

def start_game():
    clear_board()
    clear_widgets()
    board["cells"]=["","","","","","","","","",""]
    board["turn"].append("X")
    frame4()
    # frame 2 and 4 are identicle but 4 is more compact


#create a buttoon
class box:
    def __init__(self,mark,index):
        self.mark = mark
        self.index = index
    def create_button(self,l_margin,r_margin):
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
        button.clicked.connect(lambda x: self.next_Turn(button))
        self.btn = button
        return self

    def box_id(self):
        return self.mark

    def box_index(self):
        return self.index

    def next_Turn(self, button):
        player = button.text()
        if player == "":

            if board["turn"][-1]=="X":
                self.mark_X(button)
            else:
                self.mark_O(button)

    def update_check(self,mark,index):
        cell = board["cells"]
        #print(cell)
        cell[index] = mark
        board["cells"].pop()
        board["cells"].append(cell)
        #print(cell)

    def mark_X(self,button):
        button.setText('X')
        self.mark = 'X'
        board['turn'].pop()
        board['turn'].append('O')
        # print("appended an O :   = "+board['turn'])
        self.update_check(self.mark,self.index)
        #                   print("appended an X :   = "+board['cell'])
        if Check_Winning():
            print("someone one with X")
            cells = board['cells']
            print(cells)

    def mark_O(self,button):
        self.mark = 'O'
        button.setText('O')
        board['turn'].pop()
        board['turn'].append('X')
        self.update_check(self.mark,self.index)
        #print("appended an O :   = " + board['cell'][-1])
        # I don't think I need the boolean aspect, also check the mark_X function
        if Check_Winning():
            print("someone won with O")


    def addWidget(self,col,row):
        grid.addWidget(self.btn,col,row)

def Check_Winning():
    if columns_check() or row_check() or diagnal_check():
            score_keeper["winner"].append(board["turn"][-1])
            clear_board()
            clear_widgets()
            #round_winner(score_keeper)
            frame3()
            return True
    elif tie_check():
        score_keeper["winner"].append("T")
        clear_board()
        clear_widgets()
        frame3()
        return True
    # else:
    #     print("all returned false ")
def row_check():
    cells = board["cells"][-1]
    for i in range(0,3):
        m = i*3
        if cells[0+m] == cells[1+m] == cells[2+m] != "":
            return True

def columns_check():
    cells = board["cells"][-1]
    for i in range(0,3):
        if cells[i] == cells[i+3] == cells[i+6] != "":
            return True

def diagnal_check():
    cells = board["cells"][-1]
    if cells[0]==cells[4]==cells[8] != "":
        return True
    if cells[2] == cells[4] == cells[6] != "":
        return True
    else:
        return False
def tie_check():
    cells = board["cells"][-1]
    tie = False
    try:
     loc = cells.index("")
     print(loc)
    except:
        tie = True
        #print( tie + " this should only be True")
    #print(tie)
    return tie
    # for mark in cells:
    #     print(mark)
    #     if mark  == "":
    #         return tie
    #         print(" a blank spot was detected. ")
        #     return False
        # else:
        #     return True
    #return False
def clear_board():
    for mark in board:
        if board[mark] != []:
            for i in range(0,len(board[mark])):
                board[mark].pop()

def round_winner(self,winnerPlayer):
    if winnerPlayer["turn"][-1] == "O":
        winnerPlayer["winner"].append("O")
    elif winnerPlayer["turn"][-1] == "X":
        winnerPlayer["winner"].append("X")
    else:
        winnerPlayer["winner"].append("T")

    print(winnerPlayer["winner"][-1] + "  winner of the round")
def clear_widgets():

    for i in reversed(range(grid.count())):
        grid.itemAt(i).widget().setParent(None)


def frame1():
    #intro logo page

    image = QPixmap('banner1.png')
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    board["logo"].append(logo)

    #play button
    button = QPushButton("Player 1 Vs Player 2")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        '''
        *{
            border: 4px solid '#E66912';
            border-radius: 45px;
            font-size: 35px;
            color: 'white';
            padding: 25px 0;
            margin: 20px 200px;
        }
        *:hover{
            background: '#E66912';
        }
        '''
    )
    board["button"].append(button)
    button.clicked.connect(start_game)
    #grid.addWidget(board["logo"][-1],0,0,1,2)
    #grid.addWidget(board["button"][-1],1,0,1,2)
    # Comp Vs People button
    button_CompVPlayer = QPushButton('Player 1 Vs COMP')
    button_CompVPlayer.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button_CompVPlayer.setStyleSheet(
        '''
        *{
            border: 4px solid '#E66912';
            border-radius: 45px;
            font-size: 35px;
            color: 'white';
            padding: 25px 0 ;
            margin: 10px 200px;
        }
        *:hover{
            background: '#E66912';
        }
        '''
    )
    board["button"].append(button_CompVPlayer)
    button_CompVPlayer.clicked.connect(AI_frame)

    #bottom banner
    bottom_image = QPixmap('bottomLogo.JPG')
    bottom_logo = QLabel()
    bottom_logo.setPixmap(bottom_image)
    bottom_logo.setAlignment(QtCore.Qt.AlignCenter)
    bottom_logo.setStyleSheet("margin-top: 100px; margin-bottom: 20px;")
    board["logoBottom"].append(bottom_logo)

    grid.addWidget(board["logo"][0], 0, 0, 1, 2)
    grid.addWidget(board["button"][0], 1, 0, 1, 2)
    grid.addWidget(board["button"][-1], 2, 0, 1, 2)
    grid.addWidget(board["logoBottom"][0], 3, 0, 1, 2)
def AI_frame():
    print('love the cat. This is wehre the AI button would go')
def frame2():

    image = QPixmap('banner2.png')
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 0px; margin-bottom: 0px;")
    board["logo"].append(logo)

    B_image = QPixmap('bottomLogo.JPG')
    Blogo = QLabel()
    Blogo.setPixmap(B_image)
    Blogo.setAlignment(QtCore.Qt.AlignCenter)
    Blogo.setStyleSheet("margin-top: 10px; martin-bottom: 50px;")
    board["logoBottom"].append(Blogo)

    button1 = box("",0).create_button( 100, 1)
    button2 = box("",1).create_button( 50, 50)
    button3 = box("",2).create_button( 1, 100)

    button4 = box("",3).create_button(100, 1)
    button5 = box("",4).create_button(50, 50)
    button6 = box("",5).create_button(1, 100)

    button7 = box("",6).create_button(100, 1)
    button8 = box("",7).create_button(50, 50)
    button9 = box("",8).create_button(1, 100)


    #board["cells"].append(clicker)

    grid.addWidget(board["logo"][0], 0, 0, 1, 3)

    box.addWidget(button1,1,0)
    box.addWidget(button2,1,1)
    box.addWidget(button3,1,2)

    box.addWidget(button4, 2, 0)
    box.addWidget(button5, 2, 1)
    box.addWidget(button6, 2, 2)

    box.addWidget(button7, 3, 0)
    box.addWidget(button8, 3, 1)
    box.addWidget(button9, 3, 2)

#### you are trying to center teh bottom banner but don't know how I think it has something to do with these bottom two lines

    grid.addWidget(board["logoBottom"][-1], 4, 0, 1, 3)

def frame3():
    image = QPixmap("banner1.PNG")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    board["logo"].append(logo)
    grid.addWidget(board["logo"][-1],0,0,1,3)

    # probabaly don't need this print part
    print(score_keeper["winner"])
    print('????')
    print(board["turn"])
    print(';;;;;;;')

    button = QPushButton("Play Again ?")
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
    button.clicked.connect(start_game)
    grid.addWidget(board["logo"][-1], 0, 0, 1, 2)
    grid.addWidget(board["button"][-1], 1, 0, 1, 2)

    # you want to figure out a way to acknowledge the winner of a past round and keep score for the next two rounds
def toplogo():
    image = QPixmap("banner1.PNG")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    board["logo"].append(logo)
    grid.addWidget(board["logo"][-1], 0, 0, 1, 3)
def bottomlogo():
    bottom_image = QPixmap('bottomLogo.JPG')
    bottom_logo = QLabel()
    bottom_logo.setPixmap(bottom_image)
    bottom_logo.setAlignment(QtCore.Qt.AlignCenter)
    bottom_logo.setStyleSheet("margin-top: 100px; margin-bottom: 20px;")
    board["logoBottom"].append(bottom_logo)
    grid.addWidget(board["logoBottom"][0], 4, 0, 1, 3)

def gridBoard():
    #board["turn"].append("X")
    button1 = box("", 0).create_button(100, 1)
    button2 = box("", 1).create_button(50, 50)
    button3 = box("", 2).create_button(1, 100)

    button4 = box("", 3).create_button(100, 1)
    button5 = box("", 4).create_button(50, 50)
    button6 = box("", 5).create_button(1, 100)

    button7 = box("", 6).create_button(100, 1)
    button8 = box("", 7).create_button(50, 50)
    button9 = box("", 8).create_button(1, 100)

    # board["cells"].append(clicker)

    box.addWidget(button1, 1, 0)
    box.addWidget(button2, 1, 1)
    box.addWidget(button3, 1, 2)

    box.addWidget(button4, 2, 0)
    box.addWidget(button5, 2, 1)
    box.addWidget(button6, 2, 2)

    box.addWidget(button7, 3, 0)
    box.addWidget(button8, 3, 1)
    box.addWidget(button9, 3, 2)

def stGM():
    clear_board()
    clear_widgets()
    board["cells"] = ["", "", "", "", "", "", "", "", "", ""]
    board["turn"].append("X")
    frame4

def frame4():
    stGM()
    toplogo()
    gridBoard()
    bottomlogo()
# I think this should display the winner and provide the option to quit, play again in the same mode or go back to the main menue.
def frame5():
    toplogo()
    