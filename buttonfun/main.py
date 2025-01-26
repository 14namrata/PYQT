import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

from fun import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow
        
        self.Button1 = QPushButton("Button1", self)
        self.Button1.setGeometry(72, 137, 221, 41)
        self.Button1.clicked.connect(self.Button1_clicked)
        self.Button1.setStyleSheet("background-color: rgb(118, 118, 118); color: rgb(255, 255, 255);")

        self.Button2 = QPushButton("Button2", self)
        self.Button2.setGeometry(300, 137, 221, 41)
        self.Button2.clicked.connect(self.Button2_clicked)
        self.Button2.setStyleSheet("background-color: rgb(118, 118, 118); color: rgb(255, 255, 255);")

        self.lineEdit = QLineEdit(self)  # This is where the text will show up
        self.lineEdit.setGeometry(50, 300, 300, 40) 
        self.lineEdit.setAlignment(Qt.AlignCenter)
    def Button1_clicked(self):
        self.lineEdit.setText("Button 1 is clicked")
    def Button2_clicked(self):
        self.lineEdit.setText("Button 2 clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Main()
    
    MainWindow.show()
    sys.exit(app.exec_())

    
    