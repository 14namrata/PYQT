import sys
from PyQt5 import QtWidgets
from win_ui import Ui_MainWindow


class MainWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.num_of_clicks = 0
        self.ui.pushButton_click.pressed.connect(self.update_clicks)
        self.show()

    def update_clicks(self):
        self.num_of_clicks += 1
        self.ui.click_count_label.setText(f"No. of Clicks:{self.num_of_clicks}")


if __name__=="__main__":
    
    app=QtWidgets.QApplication(sys.argv)
    obj=MainWin()
    sys.exit(app.exec_())

