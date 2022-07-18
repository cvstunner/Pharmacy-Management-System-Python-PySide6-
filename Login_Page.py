# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login_Page.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(410, 500)
        Form.setMinimumSize(QSize(410, 500))
        Form.setMaximumSize(QSize(410, 500))
        Form.setStyleSheet(u"background-color: rgb(48, 48, 123);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 20)
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.login_exit_label = QLabel(self.frame_2)
        self.login_exit_label.setObjectName(u"login_exit_label")
        self.login_exit_label.setGeometry(QRect(370, 20, 21, 20))
        self.login_exit_label.setStyleSheet(u"#login_exit_label{\n"
"	color: rgba(255, 255, 255,205);\n"
"	font: 900 14pt \"Arial Black\";\n"
"}")

        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(7)
        self.gridLayout.setContentsMargins(20, -1, 20, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 250))
        font = QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(243, 243, 243);\n"
"font: 20pt \"Viner Hand ITC\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(330, 35))
        self.label_2.setMaximumSize(QSize(330, 35))
        self.label_2.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: rgb(238, 238, 238);")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.username_edit = QLineEdit(self.frame)
        self.username_edit.setObjectName(u"username_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.username_edit.sizePolicy().hasHeightForWidth())
        self.username_edit.setSizePolicy(sizePolicy1)
        self.username_edit.setMinimumSize(QSize(330, 35))
        self.username_edit.setMaximumSize(QSize(330, 35))
        self.username_edit.setStyleSheet(u"border:1px solid rgba(255,255,255,255);\n"
"color: rgb(235, 235, 235);\n"
"border-radius:2px;")

        self.gridLayout.addWidget(self.username_edit, 2, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(330, 0))
        self.label_3.setMaximumSize(QSize(330, 35))
        self.label_3.setSizeIncrement(QSize(460, 35))
        self.label_3.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: rgb(240, 240, 240);")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.password_edit = QLineEdit(self.frame)
        self.password_edit.setObjectName(u"password_edit")
        sizePolicy.setHeightForWidth(self.password_edit.sizePolicy().hasHeightForWidth())
        self.password_edit.setSizePolicy(sizePolicy)
        self.password_edit.setMinimumSize(QSize(330, 35))
        self.password_edit.setMaximumSize(QSize(330, 35))
        self.password_edit.setStyleSheet(u"border:1px solid rgba(255,255,255,255);\n"
"color: rgb(235, 235, 235);\n"
"border-radius:2px;")
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.password_edit, 4, 0, 1, 1)

        self.login_btn = QPushButton(self.frame)
        self.login_btn.setObjectName(u"login_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy2)
        self.login_btn.setMinimumSize(QSize(330, 0))
        self.login_btn.setMaximumSize(QSize(330, 16777215))
        self.login_btn.setStyleSheet(u"font: 10pt \"Arial\";\n"
"background-color: rgb(220, 220, 220);")

        self.gridLayout.addWidget(self.login_btn, 5, 0, 1, 1)

        self.login_signup_btn = QPushButton(self.frame)
        self.login_signup_btn.setObjectName(u"login_signup_btn")
        self.login_signup_btn.setMinimumSize(QSize(330, 0))
        self.login_signup_btn.setMaximumSize(QSize(330, 16777215))
        self.login_signup_btn.setStyleSheet(u"font: 10pt \"Arial\";\n"
"background-color: rgb(220, 220, 220);")

        self.gridLayout.addWidget(self.login_signup_btn, 6, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.login_exit_label.setText(QCoreApplication.translate("Form", u"X", None))
        self.label.setText(QCoreApplication.translate("Form", u"Login Page", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Password", None))
        self.login_btn.setText(QCoreApplication.translate("Form", u"Login", None))
        self.login_signup_btn.setText(QCoreApplication.translate("Form", u"Sign-in", None))
    # retranslateUi

