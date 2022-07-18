# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Main_Widget(object):
    def setupUi(self, Main_Widget):
        if not Main_Widget.objectName():
            Main_Widget.setObjectName(u"Main_Widget")
        Main_Widget.resize(1000, 750)
        Main_Widget.setMinimumSize(QSize(1000, 750))
        Main_Widget.setMaximumSize(QSize(1000, 750))
        Main_Widget.setStyleSheet(u"#Main_Widget{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame = QFrame(Main_Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 175, 750))
        self.frame.setMinimumSize(QSize(175, 750))
        self.frame.setMaximumSize(QSize(175, 750))
        self.frame.setStyleSheet(u"background-color: rgb(48, 48, 123);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 250, 175, 125))
        self.frame_2.setMinimumSize(QSize(175, 125))
        self.frame_2.setMaximumSize(QSize(175, 125))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(-1)
        self.frame_2.setMidLineWidth(-1)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_label = QLabel(self.frame_2)
        self.home_label.setObjectName(u"home_label")
        self.home_label.setMinimumSize(QSize(175, 25))
        self.home_label.setMaximumSize(QSize(175, 25))
        self.home_label.setStyleSheet(u"#home_label{\n"
"	font: 12pt \"Arial\";\n"
"	color: rgba(255, 255, 255, 200);\n"
"}\n"
"\n"
"#home_label:hover{\n"
"	background-color: rgba(255, 255, 255,50);\n"
"}")
        self.home_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.home_label)

        self.stock_label = QLabel(self.frame_2)
        self.stock_label.setObjectName(u"stock_label")
        self.stock_label.setMinimumSize(QSize(175, 25))
        self.stock_label.setMaximumSize(QSize(175, 25))
        self.stock_label.setStyleSheet(u"#stock_label{\n"
"	font: 12pt \"Arial\";\n"
"	color: rgba(255, 255, 255, 200);\n"
"}\n"
"\n"
"#stock_label:hover{\n"
"	background-color: rgba(255, 255, 255,50);\n"
"}")
        self.stock_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.stock_label)

        self.supplier_label = QLabel(self.frame_2)
        self.supplier_label.setObjectName(u"supplier_label")
        self.supplier_label.setMinimumSize(QSize(175, 25))
        self.supplier_label.setMaximumSize(QSize(175, 25))
        self.supplier_label.setStyleSheet(u"#supplier_label{\n"
"	font: 12pt \"Arial\";\n"
"	color: rgba(255, 255, 255, 200);\n"
"}\n"
"\n"
"#supplier_label:hover{\n"
"	background-color: rgba(255, 255, 255,50);\n"
"}")
        self.supplier_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.supplier_label)

        self.invoice_label = QLabel(self.frame_2)
        self.invoice_label.setObjectName(u"invoice_label")
        self.invoice_label.setMinimumSize(QSize(175, 25))
        self.invoice_label.setMaximumSize(QSize(175, 25))
        self.invoice_label.setStyleSheet(u"#invoice_label{\n"
"	font: 12pt \"Arial\";\n"
"	color: rgba(255, 255, 255, 200);\n"
"}\n"
"\n"
"#invoice_label:hover{\n"
"	background-color: rgba(255, 255, 255,50);\n"
"}")
        self.invoice_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.invoice_label)

        self.admin_label = QLabel(self.frame_2)
        self.admin_label.setObjectName(u"admin_label")
        self.admin_label.setMinimumSize(QSize(175, 25))
        self.admin_label.setMaximumSize(QSize(175, 25))
        self.admin_label.setStyleSheet(u"#admin_label{\n"
"	font: 12pt \"Arial\";\n"
"	color: rgba(255, 255, 255, 200);\n"
"}\n"
"\n"
"#admin_label:hover{\n"
"	background-color: rgba(255, 255, 255,50);\n"
"}")
        self.admin_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.admin_label)

        self.Push = QLabel(self.frame)
        self.Push.setObjectName(u"Push")
        self.Push.setGeometry(QRect(0, 70, 175, 20))
        self.Push.setMinimumSize(QSize(175, 0))
        self.Push.setMaximumSize(QSize(175, 16777215))
        self.Push.setStyleSheet(u"color: rgb(238, 238, 238);\n"
"font: 700 14pt \"Segoe Script\";")
        self.Push.setAlignment(Qt.AlignCenter)
        self.stackedWidget = QStackedWidget(Main_Widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(175, 0, 825, 750))
        self.stackedWidget.setMinimumSize(QSize(825, 750))
        self.stackedWidget.setMaximumSize(QSize(875, 750))
        self.stackedWidget.setStyleSheet(u"#header_title_2{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.exit_label_2 = QLabel(self.home_page)
        self.exit_label_2.setObjectName(u"exit_label_2")
        self.exit_label_2.setGeometry(QRect(785, 0, 41, 40))
        self.exit_label_2.setStyleSheet(u"#exit_label_2{\n"
"	font: 900 14pt \"Arial Black\";\n"
"}\n"
"\n"
"#exit_label_2::hover{\n"
"	background-color:rgba(219, 68, 55, 255);\n"
"	color:rgba(255,255,255,255);\n"
"}\n"
"")
        self.exit_label_2.setAlignment(Qt.AlignCenter)
        self.address_label = QLabel(self.home_page)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setGeometry(QRect(70, 230, 301, 20))
        self.user_name_lineEdit = QLineEdit(self.home_page)
        self.user_name_lineEdit.setObjectName(u"user_name_lineEdit")
        self.user_name_lineEdit.setGeometry(QRect(70, 180, 301, 26))
        self.user_drug_price_lineEdit = QLineEdit(self.home_page)
        self.user_drug_price_lineEdit.setObjectName(u"user_drug_price_lineEdit")
        self.user_drug_price_lineEdit.setEnabled(True)
        self.user_drug_price_lineEdit.setGeometry(QRect(70, 420, 301, 26))
        self.user_drug_price_lineEdit.setReadOnly(True)
        self.user_drugs_refresh_btn = QPushButton(self.home_page)
        self.user_drugs_refresh_btn.setObjectName(u"user_drugs_refresh_btn")
        self.user_drugs_refresh_btn.setGeometry(QRect(760, 460, 31, 29))
        self.users_drugs_list_table = QTableWidget(self.home_page)
        self.users_drugs_list_table.setObjectName(u"users_drugs_list_table")
        self.users_drugs_list_table.setGeometry(QRect(30, 490, 761, 231))
        self.users_drugs_list_table.setMinimumSize(QSize(761, 231))
        self.users_drugs_list_table.setMaximumSize(QSize(761, 231))
        self.users_drugs_list_table.setStyleSheet(u"#users_drugs_list_table{\n"
"	border:1px solid rgba(0,0,0,255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background:rgba(48, 48, 123, 75);\n"
"	color:black;\n"
"}")
        self.users_drugs_list_table.setFrameShape(QFrame.NoFrame)
        self.users_drugs_list_table.setFrameShadow(QFrame.Plain)
        self.users_drugs_list_table.setLineWidth(0)
        self.users_drugs_list_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.users_drugs_list_table.setAlternatingRowColors(True)
        self.users_drugs_list_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.users_drugs_list_table.setShowGrid(True)
        self.users_drugs_list_table.setSortingEnabled(True)
        self.users_drugs_list_table.horizontalHeader().setCascadingSectionResizes(True)
        self.users_drugs_list_table.horizontalHeader().setMinimumSectionSize(20)
        self.users_drugs_list_table.horizontalHeader().setDefaultSectionSize(108)
        self.users_drugs_list_table.horizontalHeader().setProperty("showSortIndicator", True)
        self.users_drugs_list_table.horizontalHeader().setStretchLastSection(True)
        self.users_drugs_list_table.verticalHeader().setVisible(False)
        self.users_drugs_list_table.verticalHeader().setHighlightSections(False)
        self.label_12 = QLabel(self.home_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(450, 150, 301, 20))
        self.label_14 = QLabel(self.home_page)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(70, 390, 301, 20))
        self.user_drug_company_comboBox = QComboBox(self.home_page)
        self.user_drug_company_comboBox.setObjectName(u"user_drug_company_comboBox")
        self.user_drug_company_comboBox.setGeometry(QRect(450, 260, 301, 26))
        self.user_address_lineEdit = QLineEdit(self.home_page)
        self.user_address_lineEdit.setObjectName(u"user_address_lineEdit")
        self.user_address_lineEdit.setGeometry(QRect(70, 260, 301, 26))
        self.user_phone_lineEdit = QLineEdit(self.home_page)
        self.user_phone_lineEdit.setObjectName(u"user_phone_lineEdit")
        self.user_phone_lineEdit.setGeometry(QRect(450, 180, 301, 26))
        self.user_phone_lineEdit.setMaxLength(10)
        self.header_frame_4 = QFrame(self.home_page)
        self.header_frame_4.setObjectName(u"header_frame_4")
        self.header_frame_4.setGeometry(QRect(0, 40, 825, 80))
        self.header_frame_4.setMinimumSize(QSize(825, 80))
        self.header_frame_4.setMaximumSize(QSize(825, 80))
        self.header_frame_4.setStyleSheet(u"#header_frame_4{\n"
"	background-color: rgba(48, 48, 123, 100);\n"
"}")
        self.header_frame_4.setFrameShape(QFrame.NoFrame)
        self.header_frame_4.setFrameShadow(QFrame.Plain)
        self.header_frame_4.setLineWidth(0)
        self.gridLayout_6 = QGridLayout(self.header_frame_4)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.header_title_6 = QLabel(self.header_frame_4)
        self.header_title_6.setObjectName(u"header_title_6")
        self.header_title_6.setMinimumSize(QSize(825, 80))
        self.header_title_6.setMaximumSize(QSize(825, 80))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.header_title_6.setFont(font)
        self.header_title_6.setStyleSheet(u"#header_title_6{\n"
"	color: rgba(0, 0, 0, 175);\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.header_title_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.header_title_6, 2, 0, 1, 1)

        self.pushButton = QPushButton(self.header_frame_4)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_6.addWidget(self.pushButton, 3, 0, 1, 1)

        self.label_13 = QLabel(self.home_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(450, 230, 301, 20))
        self.frame_4 = QFrame(self.home_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(450, 420, 300, 30))
        self.frame_4.setMinimumSize(QSize(300, 30))
        self.frame_4.setMaximumSize(QSize(300, 30))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(14)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.add_users_drug_btn = QPushButton(self.frame_4)
        self.add_users_drug_btn.setObjectName(u"add_users_drug_btn")
        self.add_users_drug_btn.setMinimumSize(QSize(65, 0))
        self.add_users_drug_btn.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_5.addWidget(self.add_users_drug_btn)

        self.delete_drug_btn_4 = QPushButton(self.frame_4)
        self.delete_drug_btn_4.setObjectName(u"delete_drug_btn_4")
        self.delete_drug_btn_4.setMinimumSize(QSize(65, 0))
        self.delete_drug_btn_4.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_5.addWidget(self.delete_drug_btn_4)

        self.user_drug_total_price_lineEdit = QLineEdit(self.frame_4)
        self.user_drug_total_price_lineEdit.setObjectName(u"user_drug_total_price_lineEdit")
        self.user_drug_total_price_lineEdit.setEnabled(True)
        self.user_drug_total_price_lineEdit.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.user_drug_total_price_lineEdit)

        self.user_buy_drug_btn = QPushButton(self.frame_4)
        self.user_buy_drug_btn.setObjectName(u"user_buy_drug_btn")
        self.user_buy_drug_btn.setMinimumSize(QSize(65, 0))
        self.user_buy_drug_btn.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_5.addWidget(self.user_buy_drug_btn)

        self.label_11 = QLabel(self.home_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(70, 310, 301, 20))
        self.label_15 = QLabel(self.home_page)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(450, 310, 301, 20))
        self.label_10 = QLabel(self.home_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(70, 150, 301, 20))
        self.user_drug_name_combobox = QComboBox(self.home_page)
        self.user_drug_name_combobox.setObjectName(u"user_drug_name_combobox")
        self.user_drug_name_combobox.setGeometry(QRect(70, 340, 301, 26))
        self.user_drug_quantity_combobox = QComboBox(self.home_page)
        self.user_drug_quantity_combobox.addItem("")
        self.user_drug_quantity_combobox.addItem("")
        self.user_drug_quantity_combobox.addItem("")
        self.user_drug_quantity_combobox.addItem("")
        self.user_drug_quantity_combobox.addItem("")
        self.user_drug_quantity_combobox.addItem("")
        self.user_drug_quantity_combobox.setObjectName(u"user_drug_quantity_combobox")
        self.user_drug_quantity_combobox.setGeometry(QRect(450, 340, 301, 26))
        self.stackedWidget.addWidget(self.home_page)
        self.supplier_page = QWidget()
        self.supplier_page.setObjectName(u"supplier_page")
        self.header_frame_2 = QFrame(self.supplier_page)
        self.header_frame_2.setObjectName(u"header_frame_2")
        self.header_frame_2.setGeometry(QRect(0, 40, 825, 80))
        self.header_frame_2.setMinimumSize(QSize(825, 80))
        self.header_frame_2.setMaximumSize(QSize(825, 80))
        self.header_frame_2.setStyleSheet(u"#header_frame_2{\n"
"	background-color: rgba(48, 48, 123, 100);\n"
"}")
        self.header_frame_2.setFrameShape(QFrame.NoFrame)
        self.header_frame_2.setFrameShadow(QFrame.Plain)
        self.header_frame_2.setLineWidth(0)
        self.gridLayout_2 = QGridLayout(self.header_frame_2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_title_2 = QLabel(self.header_frame_2)
        self.header_title_2.setObjectName(u"header_title_2")
        self.header_title_2.setMinimumSize(QSize(825, 80))
        self.header_title_2.setMaximumSize(QSize(825, 80))
        self.header_title_2.setFont(font)
        self.header_title_2.setStyleSheet(u"#header_title_2{\n"
"	color: rgba(0, 0, 0, 175);\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.header_title_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.header_title_2, 0, 0, 1, 1)

        self.suppliers_refresh_btn = QPushButton(self.supplier_page)
        self.suppliers_refresh_btn.setObjectName(u"suppliers_refresh_btn")
        self.suppliers_refresh_btn.setGeometry(QRect(760, 460, 31, 29))
        self.supp_drrug_company_lineEdit = QLineEdit(self.supplier_page)
        self.supp_drrug_company_lineEdit.setObjectName(u"supp_drrug_company_lineEdit")
        self.supp_drrug_company_lineEdit.setEnabled(True)
        self.supp_drrug_company_lineEdit.setGeometry(QRect(70, 420, 301, 26))
        self.supp_drrug_company_lineEdit.setReadOnly(False)
        self.supp_phone_lineEdit = QLineEdit(self.supplier_page)
        self.supp_phone_lineEdit.setObjectName(u"supp_phone_lineEdit")
        self.supp_phone_lineEdit.setGeometry(QRect(450, 180, 301, 26))
        self.supp_phone_lineEdit.setMaxLength(10)
        self.address_label_2 = QLabel(self.supplier_page)
        self.address_label_2.setObjectName(u"address_label_2")
        self.address_label_2.setGeometry(QRect(70, 230, 301, 20))
        self.supp_name_lineEdit = QLineEdit(self.supplier_page)
        self.supp_name_lineEdit.setObjectName(u"supp_name_lineEdit")
        self.supp_name_lineEdit.setGeometry(QRect(70, 180, 301, 26))
        self.label_16 = QLabel(self.supplier_page)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(450, 150, 301, 20))
        self.label_17 = QLabel(self.supplier_page)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(450, 230, 301, 20))
        self.label_18 = QLabel(self.supplier_page)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(70, 150, 301, 20))
        self.supp_email_lineEdit = QLineEdit(self.supplier_page)
        self.supp_email_lineEdit.setObjectName(u"supp_email_lineEdit")
        self.supp_email_lineEdit.setGeometry(QRect(70, 260, 301, 26))
        self.supp_id_proof_combobox = QComboBox(self.supplier_page)
        self.supp_id_proof_combobox.addItem("")
        self.supp_id_proof_combobox.addItem("")
        self.supp_id_proof_combobox.addItem("")
        self.supp_id_proof_combobox.addItem("")
        self.supp_id_proof_combobox.setObjectName(u"supp_id_proof_combobox")
        self.supp_id_proof_combobox.setGeometry(QRect(70, 340, 301, 26))
        self.frame_5 = QFrame(self.supplier_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(450, 420, 300, 30))
        self.frame_5.setMinimumSize(QSize(300, 30))
        self.frame_5.setMaximumSize(QSize(300, 30))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(14)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.add_supplier_btn = QPushButton(self.frame_5)
        self.add_supplier_btn.setObjectName(u"add_supplier_btn")
        self.add_supplier_btn.setMinimumSize(QSize(65, 0))
        self.add_supplier_btn.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_6.addWidget(self.add_supplier_btn)

        self.update_drug_btn_2 = QPushButton(self.frame_5)
        self.update_drug_btn_2.setObjectName(u"update_drug_btn_2")
        self.update_drug_btn_2.setMinimumSize(QSize(65, 0))
        self.update_drug_btn_2.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_6.addWidget(self.update_drug_btn_2)

        self.delete_drug_btn_5 = QPushButton(self.frame_5)
        self.delete_drug_btn_5.setObjectName(u"delete_drug_btn_5")
        self.delete_drug_btn_5.setMinimumSize(QSize(65, 0))
        self.delete_drug_btn_5.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_6.addWidget(self.delete_drug_btn_5)

        self.supplier_search_btn = QPushButton(self.frame_5)
        self.supplier_search_btn.setObjectName(u"supplier_search_btn")
        self.supplier_search_btn.setMinimumSize(QSize(65, 0))
        self.supplier_search_btn.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_6.addWidget(self.supplier_search_btn)

        self.suppliers_table = QTableWidget(self.supplier_page)
        self.suppliers_table.setObjectName(u"suppliers_table")
        self.suppliers_table.setGeometry(QRect(30, 490, 761, 231))
        self.suppliers_table.setMinimumSize(QSize(761, 231))
        self.suppliers_table.setMaximumSize(QSize(761, 231))
        self.suppliers_table.setStyleSheet(u"#suppliers_table{\n"
"	border:1px solid rgba(0,0,0,255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background:rgba(48, 48, 123, 75);\n"
"	color:black;\n"
"}")
        self.suppliers_table.setFrameShape(QFrame.NoFrame)
        self.suppliers_table.setFrameShadow(QFrame.Plain)
        self.suppliers_table.setLineWidth(0)
        self.suppliers_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.suppliers_table.setAlternatingRowColors(True)
        self.suppliers_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.suppliers_table.setShowGrid(True)
        self.suppliers_table.setSortingEnabled(True)
        self.suppliers_table.horizontalHeader().setCascadingSectionResizes(True)
        self.suppliers_table.horizontalHeader().setMinimumSectionSize(20)
        self.suppliers_table.horizontalHeader().setDefaultSectionSize(108)
        self.suppliers_table.horizontalHeader().setProperty("showSortIndicator", True)
        self.suppliers_table.horizontalHeader().setStretchLastSection(True)
        self.suppliers_table.verticalHeader().setVisible(False)
        self.suppliers_table.verticalHeader().setHighlightSections(False)
        self.label_19 = QLabel(self.supplier_page)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(70, 390, 301, 20))
        self.exit_label_3 = QLabel(self.supplier_page)
        self.exit_label_3.setObjectName(u"exit_label_3")
        self.exit_label_3.setGeometry(QRect(785, 0, 41, 40))
        self.exit_label_3.setStyleSheet(u"#exit_label_3{\n"
"	font: 900 14pt \"Arial Black\";\n"
"}\n"
"\n"
"#exit_label_3::hover{\n"
"	background-color:rgba(219, 68, 55, 255);\n"
"	color:rgba(255,255,255,255);\n"
"}\n"
"")
        self.exit_label_3.setAlignment(Qt.AlignCenter)
        self.label_20 = QLabel(self.supplier_page)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(70, 310, 301, 20))
        self.label_21 = QLabel(self.supplier_page)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(450, 310, 301, 20))
        self.supp_address_lineEdit = QLineEdit(self.supplier_page)
        self.supp_address_lineEdit.setObjectName(u"supp_address_lineEdit")
        self.supp_address_lineEdit.setGeometry(QRect(450, 260, 301, 26))
        self.id_number_lineEdit = QLineEdit(self.supplier_page)
        self.id_number_lineEdit.setObjectName(u"id_number_lineEdit")
        self.id_number_lineEdit.setGeometry(QRect(450, 340, 301, 26))
        self.stackedWidget.addWidget(self.supplier_page)
        self.invoice_page = QWidget()
        self.invoice_page.setObjectName(u"invoice_page")
        self.header_frame_3 = QFrame(self.invoice_page)
        self.header_frame_3.setObjectName(u"header_frame_3")
        self.header_frame_3.setGeometry(QRect(0, 40, 825, 80))
        self.header_frame_3.setMinimumSize(QSize(825, 80))
        self.header_frame_3.setMaximumSize(QSize(825, 80))
        self.header_frame_3.setStyleSheet(u"#header_frame_3{\n"
"	background-color: rgba(48, 48, 123, 100);\n"
"}")
        self.header_frame_3.setFrameShape(QFrame.NoFrame)
        self.header_frame_3.setFrameShadow(QFrame.Plain)
        self.header_frame_3.setLineWidth(0)
        self.gridLayout_3 = QGridLayout(self.header_frame_3)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.header_title_3 = QLabel(self.header_frame_3)
        self.header_title_3.setObjectName(u"header_title_3")
        self.header_title_3.setMinimumSize(QSize(825, 80))
        self.header_title_3.setMaximumSize(QSize(825, 80))
        self.header_title_3.setFont(font)
        self.header_title_3.setStyleSheet(u"#header_title_3{\n"
"	color: rgba(0, 0, 0, 175);\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.header_title_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.header_title_3, 0, 0, 1, 1)

        self.invoice_table = QTableWidget(self.invoice_page)
        self.invoice_table.setObjectName(u"invoice_table")
        self.invoice_table.setGeometry(QRect(30, 160, 761, 551))
        self.invoice_table.setStyleSheet(u"#invoice_table{\n"
"	border:1px solid rgba(0,0,0,255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	color:black;\n"
"	background:rgba(48, 48, 123, 75);\n"
"}")
        self.invoice_table.setFrameShape(QFrame.NoFrame)
        self.invoice_table.setFrameShadow(QFrame.Plain)
        self.invoice_table.setLineWidth(0)
        self.invoice_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.invoice_table.setAlternatingRowColors(True)
        self.invoice_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.invoice_table.setSortingEnabled(True)
        self.invoice_table.horizontalHeader().setCascadingSectionResizes(True)
        self.invoice_table.horizontalHeader().setMinimumSectionSize(7)
        self.invoice_table.horizontalHeader().setDefaultSectionSize(82)
        self.invoice_table.horizontalHeader().setStretchLastSection(True)
        self.invoice_table.verticalHeader().setVisible(False)
        self.invoice_table.verticalHeader().setMinimumSectionSize(0)
        self.invoice_table.verticalHeader().setHighlightSections(False)
        self.exit_label_4 = QLabel(self.invoice_page)
        self.exit_label_4.setObjectName(u"exit_label_4")
        self.exit_label_4.setGeometry(QRect(785, 0, 41, 40))
        self.exit_label_4.setStyleSheet(u"#exit_label_4{\n"
"	font: 900 14pt \"Arial Black\";\n"
"}\n"
"\n"
"#exit_label_4::hover{\n"
"	background-color:rgba(219, 68, 55, 255);\n"
"	color:rgba(255,255,255,255);\n"
"}\n"
"")
        self.exit_label_4.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.invoice_page)
        self.admin_page = QWidget()
        self.admin_page.setObjectName(u"admin_page")
        self.users_table = QTableWidget(self.admin_page)
        self.users_table.setObjectName(u"users_table")
        self.users_table.setGeometry(QRect(30, 160, 761, 551))
        self.users_table.setStyleSheet(u"#users_table{\n"
"	border:1px solid rgba(0,0,0,255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background:rgba(48, 48, 123, 75);\n"
"	color:black;\n"
"}")
        self.users_table.setFrameShape(QFrame.NoFrame)
        self.users_table.setFrameShadow(QFrame.Plain)
        self.users_table.setLineWidth(0)
        self.users_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.users_table.setAlternatingRowColors(True)
        self.users_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.users_table.setSortingEnabled(True)
        self.users_table.horizontalHeader().setCascadingSectionResizes(True)
        self.users_table.horizontalHeader().setMinimumSectionSize(7)
        self.users_table.horizontalHeader().setDefaultSectionSize(82)
        self.users_table.horizontalHeader().setStretchLastSection(True)
        self.users_table.verticalHeader().setVisible(False)
        self.users_table.verticalHeader().setMinimumSectionSize(0)
        self.users_table.verticalHeader().setHighlightSections(False)
        self.header_frame_5 = QFrame(self.admin_page)
        self.header_frame_5.setObjectName(u"header_frame_5")
        self.header_frame_5.setGeometry(QRect(0, 40, 825, 80))
        self.header_frame_5.setMinimumSize(QSize(825, 80))
        self.header_frame_5.setMaximumSize(QSize(825, 80))
        self.header_frame_5.setStyleSheet(u"#header_frame_5{\n"
"	background-color: rgba(48, 48, 123, 100);\n"
"}")
        self.header_frame_5.setFrameShape(QFrame.NoFrame)
        self.header_frame_5.setFrameShadow(QFrame.Plain)
        self.header_frame_5.setLineWidth(0)
        self.gridLayout_5 = QGridLayout(self.header_frame_5)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.header_title_5 = QLabel(self.header_frame_5)
        self.header_title_5.setObjectName(u"header_title_5")
        self.header_title_5.setMinimumSize(QSize(825, 80))
        self.header_title_5.setMaximumSize(QSize(825, 80))
        self.header_title_5.setFont(font)
        self.header_title_5.setStyleSheet(u"#header_title_5{\n"
"	color: rgba(0, 0, 0, 175);\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.header_title_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.header_title_5, 0, 0, 1, 1)

        self.exit_label_5 = QLabel(self.admin_page)
        self.exit_label_5.setObjectName(u"exit_label_5")
        self.exit_label_5.setGeometry(QRect(785, 0, 41, 40))
        self.exit_label_5.setStyleSheet(u"#exit_label_5{\n"
"	font: 900 14pt \"Arial Black\";\n"
"}\n"
"\n"
"#exit_label_5::hover{\n"
"	background-color:rgba(219, 68, 55, 255);\n"
"	color:rgba(255,255,255,255);\n"
"}\n"
"")
        self.exit_label_5.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.admin_page)
        self.stock_page = QWidget()
        self.stock_page.setObjectName(u"stock_page")
        self.label_3 = QLabel(self.stock_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 390, 301, 20))
        self.drug_manf_lineEdit = QLineEdit(self.stock_page)
        self.drug_manf_lineEdit.setObjectName(u"drug_manf_lineEdit")
        self.drug_manf_lineEdit.setGeometry(QRect(70, 340, 301, 26))
        self.drug_exp_lineEdit = QLineEdit(self.stock_page)
        self.drug_exp_lineEdit.setObjectName(u"drug_exp_lineEdit")
        self.drug_exp_lineEdit.setGeometry(QRect(450, 340, 301, 26))
        self.label_5 = QLabel(self.stock_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 230, 301, 20))
        self.label = QLabel(self.stock_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 150, 301, 20))
        self.label_7 = QLabel(self.stock_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 310, 301, 20))
        self.drugs_refresh_btn = QPushButton(self.stock_page)
        self.drugs_refresh_btn.setObjectName(u"drugs_refresh_btn")
        self.drugs_refresh_btn.setGeometry(QRect(760, 460, 31, 29))
        self.label_8 = QLabel(self.stock_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(450, 150, 301, 20))
        self.label_6 = QLabel(self.stock_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(450, 310, 301, 20))
        self.header_frame = QFrame(self.stock_page)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setGeometry(QRect(0, 40, 825, 80))
        self.header_frame.setMinimumSize(QSize(825, 80))
        self.header_frame.setMaximumSize(QSize(825, 80))
        self.header_frame.setStyleSheet(u"#header_frame{\n"
"	background-color: rgba(48, 48, 123, 100);\n"
"}")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Plain)
        self.header_frame.setLineWidth(0)
        self.gridLayout_4 = QGridLayout(self.header_frame)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.header_title_4 = QLabel(self.header_frame)
        self.header_title_4.setObjectName(u"header_title_4")
        self.header_title_4.setMinimumSize(QSize(825, 80))
        self.header_title_4.setMaximumSize(QSize(825, 80))
        self.header_title_4.setFont(font)
        self.header_title_4.setStyleSheet(u"#header_title_4{\n"
"	color: rgba(0, 0, 0, 175);\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.header_title_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.header_title_4, 0, 0, 1, 1)

        self.drug_id_lineEdit = QLineEdit(self.stock_page)
        self.drug_id_lineEdit.setObjectName(u"drug_id_lineEdit")
        self.drug_id_lineEdit.setGeometry(QRect(70, 180, 301, 26))
        self.company_comboBox = QComboBox(self.stock_page)
        self.company_comboBox.setObjectName(u"company_comboBox")
        self.company_comboBox.setGeometry(QRect(450, 180, 301, 26))
        self.frame_3 = QFrame(self.stock_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(450, 420, 300, 30))
        self.frame_3.setMinimumSize(QSize(300, 30))
        self.frame_3.setMaximumSize(QSize(300, 30))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(14)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.add_drug_btn = QPushButton(self.frame_3)
        self.add_drug_btn.setObjectName(u"add_drug_btn")
        self.add_drug_btn.setMinimumSize(QSize(65, 0))
        self.add_drug_btn.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_3.addWidget(self.add_drug_btn)

        self.update_drug_btn = QPushButton(self.frame_3)
        self.update_drug_btn.setObjectName(u"update_drug_btn")
        self.update_drug_btn.setMinimumSize(QSize(65, 0))
        self.update_drug_btn.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_3.addWidget(self.update_drug_btn)

        self.delete_drug_btn = QPushButton(self.frame_3)
        self.delete_drug_btn.setObjectName(u"delete_drug_btn")
        self.delete_drug_btn.setMinimumSize(QSize(65, 0))
        self.delete_drug_btn.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_3.addWidget(self.delete_drug_btn)

        self.search_drug_btn = QPushButton(self.frame_3)
        self.search_drug_btn.setObjectName(u"search_drug_btn")
        self.search_drug_btn.setMinimumSize(QSize(65, 0))
        self.search_drug_btn.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_3.addWidget(self.search_drug_btn)

        self.drug_quantity_lineEdit = QLineEdit(self.stock_page)
        self.drug_quantity_lineEdit.setObjectName(u"drug_quantity_lineEdit")
        self.drug_quantity_lineEdit.setGeometry(QRect(450, 260, 301, 26))
        self.label_4 = QLabel(self.stock_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(450, 230, 301, 20))
        self.drugs_table = QTableWidget(self.stock_page)
        self.drugs_table.setObjectName(u"drugs_table")
        self.drugs_table.setGeometry(QRect(30, 490, 761, 231))
        self.drugs_table.setStyleSheet(u"#drugs_table{\n"
"	border:1px solid rgba(0,0,0,255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background:rgba(48, 48, 123, 75);\n"
"	color:black;\n"
"}")
        self.drugs_table.setFrameShape(QFrame.NoFrame)
        self.drugs_table.setFrameShadow(QFrame.Plain)
        self.drugs_table.setLineWidth(0)
        self.drugs_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.drugs_table.setAlternatingRowColors(True)
        self.drugs_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.drugs_table.setShowGrid(True)
        self.drugs_table.setSortingEnabled(True)
        self.drugs_table.horizontalHeader().setCascadingSectionResizes(True)
        self.drugs_table.horizontalHeader().setMinimumSectionSize(20)
        self.drugs_table.horizontalHeader().setDefaultSectionSize(108)
        self.drugs_table.horizontalHeader().setProperty("showSortIndicator", True)
        self.drugs_table.horizontalHeader().setStretchLastSection(True)
        self.drugs_table.verticalHeader().setVisible(False)
        self.drugs_table.verticalHeader().setHighlightSections(False)
        self.exit_label = QLabel(self.stock_page)
        self.exit_label.setObjectName(u"exit_label")
        self.exit_label.setGeometry(QRect(785, 0, 41, 40))
        self.exit_label.setStyleSheet(u"#exit_label{\n"
"	font: 900 14pt \"Arial Black\";\n"
"}\n"
"\n"
"#exit_label::hover{\n"
"	background-color:rgba(219, 68, 55, 255);\n"
"	color:rgba(255,255,255,255);\n"
"}\n"
"")
        self.exit_label.setAlignment(Qt.AlignCenter)
        self.drug_price_lineEdit = QLineEdit(self.stock_page)
        self.drug_price_lineEdit.setObjectName(u"drug_price_lineEdit")
        self.drug_price_lineEdit.setGeometry(QRect(70, 260, 301, 26))
        self.drug_name_lineEdit = QLineEdit(self.stock_page)
        self.drug_name_lineEdit.setObjectName(u"drug_name_lineEdit")
        self.drug_name_lineEdit.setGeometry(QRect(70, 420, 301, 26))
        self.stackedWidget.addWidget(self.stock_page)

        self.retranslateUi(Main_Widget)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Main_Widget)
    # setupUi

    def retranslateUi(self, Main_Widget):
        Main_Widget.setWindowTitle(QCoreApplication.translate("Main_Widget", u"Widget", None))
        self.home_label.setText(QCoreApplication.translate("Main_Widget", u"Dashboard", None))
        self.stock_label.setText(QCoreApplication.translate("Main_Widget", u"Stock", None))
        self.supplier_label.setText(QCoreApplication.translate("Main_Widget", u"Supplier", None))
        self.invoice_label.setText(QCoreApplication.translate("Main_Widget", u"Invoice", None))
        self.admin_label.setText(QCoreApplication.translate("Main_Widget", u"Admin", None))
        self.Push.setText(QCoreApplication.translate("Main_Widget", u"MediMan", None))
        self.exit_label_2.setText(QCoreApplication.translate("Main_Widget", u"X", None))
        self.address_label.setText(QCoreApplication.translate("Main_Widget", u"Address", None))
        self.user_name_lineEdit.setPlaceholderText(QCoreApplication.translate("Main_Widget", u"First Middle Last", None))
        self.user_drug_price_lineEdit.setText("")
        self.user_drugs_refresh_btn.setText(QCoreApplication.translate("Main_Widget", u"R", None))
        self.label_12.setText(QCoreApplication.translate("Main_Widget", u"Phone", None))
        self.label_14.setText(QCoreApplication.translate("Main_Widget", u"Price", None))
        self.user_address_lineEdit.setText("")
        self.user_address_lineEdit.setPlaceholderText(QCoreApplication.translate("Main_Widget", u"Room/Building/Street/Locality", None))
        self.header_title_6.setText(QCoreApplication.translate("Main_Widget", u"Dashboard", None))
        self.pushButton.setText(QCoreApplication.translate("Main_Widget", u"PushButton", None))
        self.label_13.setText(QCoreApplication.translate("Main_Widget", u"Company", None))
        self.add_users_drug_btn.setText(QCoreApplication.translate("Main_Widget", u"Add", None))
        self.delete_drug_btn_4.setText(QCoreApplication.translate("Main_Widget", u"Delete", None))
        self.user_drug_total_price_lineEdit.setText("")
        self.user_buy_drug_btn.setText(QCoreApplication.translate("Main_Widget", u"Buy", None))
        self.label_11.setText(QCoreApplication.translate("Main_Widget", u"Drug Name", None))
        self.label_15.setText(QCoreApplication.translate("Main_Widget", u"Quantity", None))
        self.label_10.setText(QCoreApplication.translate("Main_Widget", u"Name", None))
        self.user_drug_name_combobox.setCurrentText("")
        self.user_drug_quantity_combobox.setItemText(0, QCoreApplication.translate("Main_Widget", u"1", None))
        self.user_drug_quantity_combobox.setItemText(1, QCoreApplication.translate("Main_Widget", u"2", None))
        self.user_drug_quantity_combobox.setItemText(2, QCoreApplication.translate("Main_Widget", u"3", None))
        self.user_drug_quantity_combobox.setItemText(3, QCoreApplication.translate("Main_Widget", u"4", None))
        self.user_drug_quantity_combobox.setItemText(4, QCoreApplication.translate("Main_Widget", u"5", None))
        self.user_drug_quantity_combobox.setItemText(5, QCoreApplication.translate("Main_Widget", u"6", None))

        self.header_title_2.setText(QCoreApplication.translate("Main_Widget", u"Supplier", None))
        self.suppliers_refresh_btn.setText(QCoreApplication.translate("Main_Widget", u"R", None))
        self.supp_drrug_company_lineEdit.setText("")
        self.address_label_2.setText(QCoreApplication.translate("Main_Widget", u"Email", None))
        self.supp_name_lineEdit.setPlaceholderText(QCoreApplication.translate("Main_Widget", u"First Middle Last", None))
        self.label_16.setText(QCoreApplication.translate("Main_Widget", u"Phone", None))
        self.label_17.setText(QCoreApplication.translate("Main_Widget", u"Address", None))
        self.label_18.setText(QCoreApplication.translate("Main_Widget", u"Name", None))
        self.supp_email_lineEdit.setText("")
        self.supp_email_lineEdit.setPlaceholderText(QCoreApplication.translate("Main_Widget", u"abc@gmail.com", None))
        self.supp_id_proof_combobox.setItemText(0, QCoreApplication.translate("Main_Widget", u"Aadhaar Card", None))
        self.supp_id_proof_combobox.setItemText(1, QCoreApplication.translate("Main_Widget", u"Pan Card", None))
        self.supp_id_proof_combobox.setItemText(2, QCoreApplication.translate("Main_Widget", u"Voting Card", None))
        self.supp_id_proof_combobox.setItemText(3, QCoreApplication.translate("Main_Widget", u"Driving License", None))

        self.supp_id_proof_combobox.setCurrentText(QCoreApplication.translate("Main_Widget", u"Aadhaar Card", None))
        self.add_supplier_btn.setText(QCoreApplication.translate("Main_Widget", u"Add", None))
        self.update_drug_btn_2.setText(QCoreApplication.translate("Main_Widget", u"Update", None))
        self.delete_drug_btn_5.setText(QCoreApplication.translate("Main_Widget", u"Delete", None))
        self.supplier_search_btn.setText(QCoreApplication.translate("Main_Widget", u"Search", None))
        self.label_19.setText(QCoreApplication.translate("Main_Widget", u"Company", None))
        self.exit_label_3.setText(QCoreApplication.translate("Main_Widget", u"X", None))
        self.label_20.setText(QCoreApplication.translate("Main_Widget", u"ID Proof", None))
        self.label_21.setText(QCoreApplication.translate("Main_Widget", u"ID Number", None))
        self.supp_address_lineEdit.setText("")
        self.supp_address_lineEdit.setPlaceholderText(QCoreApplication.translate("Main_Widget", u"Room/Building/Street/Locality", None))
        self.id_number_lineEdit.setText("")
        self.id_number_lineEdit.setPlaceholderText(QCoreApplication.translate("Main_Widget", u"XXXX XXXX XXXX", None))
        self.header_title_3.setText(QCoreApplication.translate("Main_Widget", u"Invoice", None))
        self.exit_label_4.setText(QCoreApplication.translate("Main_Widget", u"X", None))
        self.header_title_5.setText(QCoreApplication.translate("Main_Widget", u"Admin", None))
        self.exit_label_5.setText(QCoreApplication.translate("Main_Widget", u"X", None))
        self.label_3.setText(QCoreApplication.translate("Main_Widget", u"Drug Name", None))
        self.drug_manf_lineEdit.setPlaceholderText(QCoreApplication.translate("Main_Widget", u"dd/mm/yyyy", None))
        self.drug_exp_lineEdit.setPlaceholderText(QCoreApplication.translate("Main_Widget", u"dd/mm/yyyy", None))
        self.label_5.setText(QCoreApplication.translate("Main_Widget", u"Drug Price", None))
        self.label.setText(QCoreApplication.translate("Main_Widget", u"Drug id", None))
        self.label_7.setText(QCoreApplication.translate("Main_Widget", u"Manf Date", None))
        self.drugs_refresh_btn.setText(QCoreApplication.translate("Main_Widget", u"R", None))
        self.label_8.setText(QCoreApplication.translate("Main_Widget", u"Company", None))
        self.label_6.setText(QCoreApplication.translate("Main_Widget", u"Exp date", None))
        self.header_title_4.setText(QCoreApplication.translate("Main_Widget", u"Stock", None))
        self.add_drug_btn.setText(QCoreApplication.translate("Main_Widget", u"Add", None))
        self.update_drug_btn.setText(QCoreApplication.translate("Main_Widget", u"Update", None))
        self.delete_drug_btn.setText(QCoreApplication.translate("Main_Widget", u"Delete", None))
        self.search_drug_btn.setText(QCoreApplication.translate("Main_Widget", u"Search", None))
        self.label_4.setText(QCoreApplication.translate("Main_Widget", u"Quantity", None))
        self.exit_label.setText(QCoreApplication.translate("Main_Widget", u"X", None))
    # retranslateUi

