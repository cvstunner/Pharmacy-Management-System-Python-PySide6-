# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QScreen
from pyside6_uic import PySide6Ui

PySide6Ui('Login_Page.ui').toPy('Login_Page.py')  
from Login_Page import Ui_Form 

class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def show_login_page(self, boolean):
        if boolean == True:
            app = QApplication([])
            login_widget = Login()

            # Frame Center (Co-ordinates)
            screen_size = QScreen.availableGeometry(QApplication.primaryScreen())
            x = (screen_size.width() - 700)/2
            y = (screen_size.height() - 500)/2 - 15
            login_widget.move(x, y)

            login_widget.show()
            sys.exit(app.exec())
        else:
            login_widget.hide()


# if __name__ == "__main__":
#     app = QApplication([])
#     login_widget = Login()

#     # Frame Center (Co-ordinates)
#     screen_size = QScreen.availableGeometry(QApplication.primaryScreen())
#     x = (screen_size.width() - 700)/2
#     y = (screen_size.height() - 500)/2 - 15
#     login_widget.move(x, y)

#     # login_widget.show()
#     # sys.exit(app.exec())











