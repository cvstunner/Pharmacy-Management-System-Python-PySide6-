# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QScreen
from pyside6_uic import PySide6Ui

PySide6Ui('form.ui').toPy('form.py')  
from form import Ui_Widget 
PySide6Ui('Login_Page.ui').toPy('Login_Page.py')  
from Login_Page import Ui_Form 
from Login import Login 

class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.Login = Login()
            
        # self.Login.show_login_page(True)


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()

    # Frame Center (Co-ordinates)
    screen_size = QScreen.availableGeometry(QApplication.primaryScreen())
    x = (screen_size.width() - 1000)/2
    y = (screen_size.height() - 700)/2 - 15

    widget.move(x, y)
    widget.show()
    sys.exit(app.exec())