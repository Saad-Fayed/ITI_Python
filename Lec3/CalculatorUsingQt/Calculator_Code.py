#Imports
from PyQt5 import QtCore, QtGui, QtWidgets
from Saad_Calculator import Ui_MainWindow
import sys

#Initialization
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

#Code

def Zero():
    ui.lineEdit.setText(ui.lineEdit.text()+"0")

def One():
    ui.lineEdit.setText(ui.lineEdit.text()+"1")
    
def Two():
    ui.lineEdit.setText(ui.lineEdit.text()+"2")
    
def Three():
    ui.lineEdit.setText(ui.lineEdit.text()+"3")
    
def Four():
    ui.lineEdit.setText(ui.lineEdit.text()+"4")
    
def Five():
    ui.lineEdit.setText(ui.lineEdit.text()+"5")

def Six():
    ui.lineEdit.setText(ui.lineEdit.text()+"6")

def Seven():
    ui.lineEdit.setText(ui.lineEdit.text()+"7")

def Eight():
    ui.lineEdit.setText(ui.lineEdit.text()+"8")

def Nine():
    ui.lineEdit.setText(ui.lineEdit.text()+"9")

def L_Bracket():
    ui.lineEdit.setText(ui.lineEdit.text()+"(")

def R_Bracket():
    ui.lineEdit.setText(ui.lineEdit.text()+")")

def Times():
    ui.lineEdit.setText(ui.lineEdit.text() + "*")

def Divide():
    ui.lineEdit.setText(ui.lineEdit.text() + "/")

def Plus():
    ui.lineEdit.setText(ui.lineEdit.text() + "+")

def Minus():
    ui.lineEdit.setText(ui.lineEdit.text() + "-")    
    
def Dot():
    ui.lineEdit.setText(ui.lineEdit.text()+".") 
    
def Clear():
    ui.lineEdit.setText("")     
    
def Delete():
    ui.lineEdit.setText(ui.lineEdit.text()[0:-1])
    
def Equal():
    ui.lineEdit.setText(str(eval(ui.lineEdit.text())))    
    
    
    
    
#Connections
ui.pushButton_11.clicked.connect(Zero)
ui.pushButton_2.clicked.connect(One)
ui.pushButton_13.clicked.connect(Two)
ui.pushButton_14.clicked.connect(Three)
ui.pushButton_3.clicked.connect(Four)
ui.pushButton_16.clicked.connect(Five)
ui.pushButton_17.clicked.connect(Six)
ui.pushButton_4.clicked.connect(Seven)
ui.pushButton_19.clicked.connect(Eight)
ui.pushButton_20.clicked.connect(Nine)
ui.pushButton_24.clicked.connect(L_Bracket)
ui.pushButton_25.clicked.connect(R_Bracket)
ui.pushButton_18.clicked.connect(Times)
ui.pushButton_21.clicked.connect(Divide)
ui.pushButton_23.clicked.connect(Plus)
ui.pushButton_22.clicked.connect(Minus)
ui.pushButton_10.clicked.connect(Dot)
ui.pushButton_26.clicked.connect(Clear)
ui.pushButton_27.clicked.connect(Delete)
ui.pushButton_9.clicked.connect(Equal)

#Exit The Calculator GUI
sys.exit(app.exec_())