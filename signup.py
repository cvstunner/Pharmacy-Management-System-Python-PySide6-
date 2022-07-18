# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(900, 625)
        Form.setMinimumSize(QSize(900, 625))
        Form.setMaximumSize(QSize(900, 625))
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(Form)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMinimumSize(QSize(900, 80))
        self.header_frame.setMaximumSize(QSize(900, 80))
        self.header_frame.setStyleSheet(u"#header_frame{\n"
"	background-color: rgba(48, 48, 123, 150);\n"
"}")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Plain)
        self.header_frame.setLineWidth(0)
        self.gridLayout = QGridLayout(self.header_frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.header_title = QLabel(self.header_frame)
        self.header_title.setObjectName(u"header_title")
        self.header_title.setMinimumSize(QSize(900, 80))
        self.header_title.setMaximumSize(QSize(900, 80))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.header_title.setFont(font)
        self.header_title.setStyleSheet(u"#header_title{\n"
"	color: rgba(0, 0, 0, 175);\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.header_title.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.header_title, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.header_frame, 0, 0, 1, 1)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(93, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.name_lineEdit = QLineEdit(self.frame)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setGeometry(QRect(90, 80, 300, 30))
        self.name_lineEdit.setMinimumSize(QSize(300, 30))
        self.name_lineEdit.setStyleSheet(u"")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 40, 300, 30))
        self.label.setMinimumSize(QSize(300, 30))
        self.label.setStyleSheet(u"font: 11pt \"Arial\";")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 140, 300, 30))
        self.label_2.setMinimumSize(QSize(300, 30))
        self.label_2.setStyleSheet(u"font: 11pt \"Arial\";")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 240, 300, 30))
        self.label_3.setMinimumSize(QSize(300, 30))
        self.label_3.setStyleSheet(u"font: 11pt \"Arial\";")
        self.email_lineEdit = QLineEdit(self.frame)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setGeometry(QRect(90, 280, 300, 30))
        self.email_lineEdit.setMinimumSize(QSize(300, 30))
        self.age_lineEdit = QLineEdit(self.frame)
        self.age_lineEdit.setObjectName(u"age_lineEdit")
        self.age_lineEdit.setGeometry(QRect(490, 80, 300, 30))
        self.age_lineEdit.setMinimumSize(QSize(300, 30))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(490, 40, 300, 30))
        self.label_4.setMinimumSize(QSize(300, 30))
        self.label_4.setStyleSheet(u"font: 11pt \"Arial\";")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(490, 130, 300, 30))
        self.label_5.setMinimumSize(QSize(300, 30))
        self.label_5.setStyleSheet(u"font: 11pt \"Arial\";")
        self.phone_lineEdit = QLineEdit(self.frame)
        self.phone_lineEdit.setObjectName(u"phone_lineEdit")
        self.phone_lineEdit.setGeometry(QRect(490, 180, 300, 30))
        self.phone_lineEdit.setMinimumSize(QSize(300, 30))
        self.username_lineEdit = QLineEdit(self.frame)
        self.username_lineEdit.setObjectName(u"username_lineEdit")
        self.username_lineEdit.setGeometry(QRect(490, 280, 300, 30))
        self.username_lineEdit.setMinimumSize(QSize(300, 30))
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(490, 240, 300, 30))
        self.label_6.setMinimumSize(QSize(300, 30))
        self.label_6.setStyleSheet(u"font: 11pt \"Arial\";")
        self.pswd_lineEdit = QLineEdit(self.frame)
        self.pswd_lineEdit.setObjectName(u"pswd_lineEdit")
        self.pswd_lineEdit.setGeometry(QRect(90, 390, 300, 30))
        self.pswd_lineEdit.setMinimumSize(QSize(300, 30))
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(90, 350, 300, 30))
        self.label_7.setMinimumSize(QSize(300, 30))
        self.label_7.setStyleSheet(u"font: 11pt \"Arial\";")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(490, 350, 300, 30))
        self.label_8.setMinimumSize(QSize(300, 30))
        self.label_8.setStyleSheet(u"font: 11pt \"Arial\";")
        self.cnf_pswd_lineEdit = QLineEdit(self.frame)
        self.cnf_pswd_lineEdit.setObjectName(u"cnf_pswd_lineEdit")
        self.cnf_pswd_lineEdit.setGeometry(QRect(490, 390, 300, 30))
        self.cnf_pswd_lineEdit.setMinimumSize(QSize(300, 30))
        self.signup_btn = QPushButton(self.frame)
        self.signup_btn.setObjectName(u"signup_btn")
        self.signup_btn.setGeometry(QRect(90, 460, 93, 29))
        self.signup_btn.setMinimumSize(QSize(93, 0))
        self.signup_btn.setMaximumSize(QSize(93, 16777215))
        self.signup_btn.setStyleSheet(u"font: 10pt \"Arial\";")
        self.back_btn = QPushButton(self.frame)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(190, 460, 93, 29))
        self.back_btn.setMinimumSize(QSize(93, 0))
        self.back_btn.setMaximumSize(QSize(93, 16777215))
        self.back_btn.setStyleSheet(u"font: 10pt \"Arial\";")
        self.signup_exit_btn = QPushButton(self.frame)
        self.signup_exit_btn.setObjectName(u"signup_exit_btn")
        self.signup_exit_btn.setGeometry(QRect(290, 460, 93, 29))
        self.signup_exit_btn.setMinimumSize(QSize(93, 0))
        self.signup_exit_btn.setMaximumSize(QSize(93, 16777215))
        self.signup_exit_btn.setStyleSheet(u"font: 10pt \"Arial\";")
        self.gender_comboBox = QComboBox(self.frame)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")
        self.gender_comboBox.setGeometry(QRect(90, 180, 300, 30))
        self.gender_comboBox.setMinimumSize(QSize(300, 30))
        self.gender_comboBox.setMaximumSize(QSize(300, 30))

        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)


        self.retranslateUi(Form)

        self.gender_comboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.header_title.setText(QCoreApplication.translate("Form", u"SignUp", None))
        self.label.setText(QCoreApplication.translate("Form", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Gender", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Email", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Age", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Phone", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Username", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Password", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Confirm Password", None))
        self.signup_btn.setText(QCoreApplication.translate("Form", u"SignUp", None))
        self.back_btn.setText(QCoreApplication.translate("Form", u"Back", None))
        self.signup_exit_btn.setText(QCoreApplication.translate("Form", u"Exit", None))
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("Form", u"Male", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("Form", u"Female", None))
        self.gender_comboBox.setItemText(2, QCoreApplication.translate("Form", u"Others", None))

    # retranslateUi

