import sys
from PyQt5.QtWidgets import QApplication,QLabel,QPushButton,QVBoxLayout,QWidget,QFileDialog,QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from ClassOpFun import box,grid,frame1,frame2

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Love Triangle")
window.setFixedWidth(1000)
window.move(500,50)
window.setStyleSheet("Background:#0B1C48;")
# ugly green hex #08c96b
frame1()
window.setLayout(grid)
window.show()
sys.exit(app.exec())
