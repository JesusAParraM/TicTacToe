import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
#function imports
from Functions import frame1, frame2, frame3, frame4, grid

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("TicTacToe")
window.setFixedWidth(1000)
window.move(500,500)
window.setStyleSheet("background: #0B1C48;")
#161219 mat black
#BC006C hot pink
#016367 teal
#0B1C48 dark blue
#E66912 orange
#9E3A14 Burnt Sienna
frame2()
window.setLayout(grid)
window.show()

sys.exit(app.exec())