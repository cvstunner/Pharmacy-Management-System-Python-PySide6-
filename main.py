# This Python file uses the following encoding: utf-8
from Login_Page import Ui_Form
from form import Ui_Main_Widget
from signup import Ui_Form as signup_Ui_Form
import os
from pathlib import Path
import sys
import mysql.connector as con

import PySide6.QtWidgets as QtWidgets
from PySide6.QtWidgets import QApplication, QWidget, QDialog, QMessageBox, QTreeWidgetItem
from PySide6 import QtCore
from PySide6.QtCore import QFile, Qt, QDate, QRegularExpression
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QScreen, QIntValidator, QRegularExpressionValidator
from pyparsing import col
from pyside6_uic import PySide6Ui
import datetime 
from pdf_gen import Invoice 



PySide6Ui('form.ui').toPy('form.py')
PySide6Ui('Login_Page.ui').toPy('Login_Page.py')
PySide6Ui('signup.ui').toPy('signup.py')


class LoginPage(QDialog):
    def __init__(self):
        super(LoginPage, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.login_btn.clicked.connect(self.login_check)
        self.ui.login_signup_btn.clicked.connect(self.show_signup_page)
        self.ui.login_exit_label.mousePressEvent = self.login_exit_label_clicked

    def login_exit_label_clicked(self, event):
        sys.exit()

    def login_check(self):
        global status_flag 
        username = self.ui.username_edit.text()
        password = self.ui.password_edit.text()

        if username == "chetan" and password == "777":
            self.show_main_window()
            status_flag = 1
        else:
            try:
                db = con.connect(host="localhost", user="root",
                                 password="", db="testproject1")
                cursor = db.cursor()
                cursor.execute("select * from manageusers where username ='" +
                               username+"' and password = '"+password+"'")
                result = cursor.fetchone()
                if result:
                    self.show_main_window()
                    status_flag = 0
                else:
                    QMessageBox.information(self, "Login", "Invalid Creds")
                db.close()
                
            except Exception as e:
                print(e)
                print("Check your Server!")
                
    # def get_status_flag(self):
    #     return status_flag

    # def set_status_flag(self, flag):
    #     global status_flag 
    #     status_flag = flag

    def show_main_window(self):
        widget.setCurrentIndex(1)
        widget.setFixedHeight(750)
        widget.setFixedWidth(1000)
        x = (screen_size.width() - 1000)/2
        y = (screen_size.height() - 750)/2
        widget.move(x, y)

    def show_signup_page(self):
        widget.setCurrentIndex(2)
        widget.setFixedHeight(625)
        widget.setFixedWidth(900)
        x = (screen_size.width() - 900)/2
        y = (screen_size.height() - 625)/2 - 15
        widget.move(x, y)


class SignUpPage(QDialog):
    def __init__(self):
        super(SignUpPage, self).__init__()
        self.ui = signup_Ui_Form()
        self.ui.setupUi(self)
        self.ui.back_btn.clicked.connect(self.show_signup_page)
        self.ui.signup_exit_btn.clicked.connect(self.signup_exit_btn_clicked)
        self.ui.signup_btn.clicked.connect(self.sign_up)

    def sign_up(self):
        name = self.ui.name_lineEdit.text()
        age = self.ui.age_lineEdit.text()
        phone = self.ui.phone_lineEdit.text()
        email = self.ui.email_lineEdit.text()
        username = self.ui.username_lineEdit.text()
        pswd = self.ui.pswd_lineEdit.text()
        cnf_pswd = self.ui.cnf_pswd_lineEdit.text()
        gender = self.ui.gender_comboBox.currentText()

        if len(name) != 0 and len(gender) != 0 and len(phone) != 0 and len(email) != 0 and len(username) != 0 and len(pswd) != 0 and len(cnf_pswd) != 0:
            pass
        else:
            QMessageBox.information(self, "SignUp", "Each Field is Mandatory!")
            return

        if pswd == cnf_pswd:
            try:
                db = con.connect(host="localhost", user="root",
                                 password="", db="testproject1")
                registerQuerry = "insert into ManageUsers (Name, Age, Gender, Phone, Email, Username, Password, Status) values ('" + \
                    name+"', '"+age+"', '"+gender+"', '" + phone + "', '" + \
                    email+"', '" + username + "', '"+pswd+"', 'Not-Allowed') "
                cursor = db.cursor()
                cursor.execute(registerQuerry)
                db.commit()
                QMessageBox.information(self, "SignUp", "SignUp Successfully")
                print("SignUp Successfully")
                db.close()
            except Exception as e:
                print(e)
                QMessageBox.information(self, "SignUp", "Error Signing Up!")
                print("Error Signing Up!")
                db.close()
        else:
            QMessageBox.information(self, "SignUp", "Check Password!")

    def show_signup_page(self):
        widget.setCurrentIndex(0)
        widget.setFixedHeight(500)
        widget.setFixedWidth(410)
        x = (screen_size.width() - 410)/2
        y = (screen_size.height() - 500)/2 - 15
        widget.move(x, y)

    def signup_exit_btn_clicked(self):
        sys.exit()


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Main_Widget()
        self.ui.setupUi(self)
        self.inv = Invoice()
        self.ui.user_name_lineEdit.setFocus()
        # self.ui.user_drug_price_lineEdit.setEditable(False)
        self.query = "select * from drugs"
        self.populate_suppliers_query = "select * from suppliers"
        self.populate_user_drug_company_comboBox()
        self.user_drug_company_changed()

        # self.only_int = QIntValidator()
        self.only_int = QRegularExpressionValidator(QRegularExpression(r'^[0-9]*$'))
        self.only_int_str = QRegularExpressionValidator(QRegularExpression(r'^[A-Za-z0-9]*$'))
        self.address_validator = QRegularExpressionValidator(QRegularExpression(r'^[A-Za-z0-9,]*$'))
        self.only_str = QRegularExpressionValidator(QRegularExpression(r'^[A-Za-z ]*$'))
        self.email_validator = QRegularExpressionValidator(QRegularExpression(r'^[A-Za-z0-9@.]*$'))
        self.company_name_validator = QRegularExpressionValidator(QRegularExpression(r'^[A-Za-z0-9.]*$'))

        self.ui.user_name_lineEdit.setValidator(self.only_str)
        self.ui.supp_name_lineEdit.setValidator(self.only_str)
        self.ui.user_address_lineEdit.setValidator(self.address_validator)
        self.ui.supp_address_lineEdit.setValidator(self.address_validator)
        self.ui.supp_email_lineEdit.setValidator(self.email_validator)

        self.ui.user_drug_price_lineEdit.setValidator(self.only_int)
        self.ui.drug_price_lineEdit.setValidator(self.only_int)
        self.ui.drug_quantity_lineEdit.setValidator(self.only_int)
        self.ui.drug_manf_lineEdit.setValidator(self.only_int)
        self.ui.drug_exp_lineEdit.setValidator(self.only_int)
        self.ui.drug_name_lineEdit.setValidator(self.only_int_str)

        self.ui.user_phone_lineEdit.setValidator(self.only_int)
        self.ui.supp_phone_lineEdit.setValidator(self.only_int)

        self.ui.drug_id_lineEdit.setValidator(self.only_int)

        self.ui.supp_drrug_company_lineEdit.setValidator(self.company_name_validator)
        self.ui.id_number_lineEdit.setValidator(self.only_int)
        
        self.ui.users_drugs_list_table.setRowCount(0)
        self.ui.users_drugs_list_table.setColumnCount(5)
        self.ui.users_drugs_list_table.setHorizontalHeaderLabels(["Name", "Company", "Price", "Quantity", "Total Price"])
        self.ui.users_drugs_list_table.setColumnWidth(0, 148)
        self.ui.users_drugs_list_table.setColumnWidth(1, 148)
        self.ui.users_drugs_list_table.setColumnWidth(2, 148)
        self.ui.users_drugs_list_table.setColumnWidth(3, 148)
        self.ui.users_drugs_list_table.setColumnWidth(4, 148)
    
        self.ui.user_drug_total_price_lineEdit.setText('₹')
        self.ui.id_number_lineEdit.setMaxLength(12)

        self.ui.exit_label.mousePressEvent = self.exit_label_clicked
        self.ui.exit_label_2.mousePressEvent = self.exit_label_clicked
        self.ui.exit_label_3.mousePressEvent = self.exit_label_clicked
        self.ui.exit_label_4.mousePressEvent = self.exit_label_clicked
        self.ui.exit_label_5.mousePressEvent = self.exit_label_clicked

        self.ui.admin_label.mousePressEvent = self.switch_to_admin_page
        self.ui.home_label.mousePressEvent = self.home_label_clicked
        self.ui.supplier_label.mousePressEvent = self.switch_to_supplier_page
        self.ui.invoice_label.mousePressEvent = self.switch_to_ivoice_page
        self.ui.stock_label.mousePressEvent = self.switch_to_stock_page
        # self.ui.invoice_table.mousePressEvent = self.invoice_table_clicked

        self.ui.drugs_refresh_btn.clicked.connect(self.refresh_btn_clicked)
        self.ui.user_drugs_refresh_btn.clicked.connect(self.user_drugs_refresh_btn_clicked)
        self.ui.suppliers_refresh_btn.clicked.connect(self.suppliers_refresh_btn_clicked)

        self.ui.add_users_drug_btn.clicked.connect(self.add_users_drug_btn_clicked)
        self.ui.add_drug_btn.clicked.connect(self.add_drug_btn_clicked)
        self.ui.add_supplier_btn.clicked.connect(self.add_supplier_btn_clicked)
        self.ui.supplier_search_btn.clicked.connect(self.supplier_search_btn_clicked)

        self.ui.update_drug_btn.clicked.connect(self.update_drug_btn_clicked)
        self.ui.search_drug_btn.clicked.connect(self.search_drug_btn_clicked)
        self.ui.delete_drug_btn.clicked.connect(self.delete_drug_btn_clicked)
        self.ui.user_buy_drug_btn.clicked.connect(self.user_buy_drug_btn_clicked)
        self.ui.drugs_table.clicked.connect(self.drugs_table_item_clicked)
        self.ui.users_table.clicked.connect(self.clicked_item)
        self.ui.invoice_table.clicked.connect(self.invoice_table_clicked)

        self.ui.user_drug_company_comboBox.currentIndexChanged.connect(self.user_drug_company_changed)
        self.ui.user_drug_name_combobox.currentIndexChanged.connect(self.user_drug_name_changed)
        self.ui.supp_id_proof_combobox.currentIndexChanged.connect(self.supp_id_proof_combobox_changed)
        # self.ui.drug_manf•_lineEdit.setValidator(QRegExpValidator(QRegExp("(\\d+)")))
        # self.ui.drug_manf_lineEdit.textChanged.connect(self.text_changed)
        # self.ui.user_phone_lineEdit.setInputMask("0000000000") 
        self.ui.drug_manf_lineEdit.setInputMask("00/00/0000") 
        self.ui.drug_exp_lineEdit.setInputMask("00/00/0000") 

    def invoice_table_clicked(self):
        items_list = self.ui.invoice_table.selectedItems()
        user_id = items_list[0].text()
        print(user_id)

        warning_msg = QMessageBox()
        warning_msg.setIcon(QMessageBox.Question)
        warning_msg.setText("Do Want Print Invoice?")
        warning_msg.setWindowTitle("Question")
        warning_msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        if warning_msg.exec() == QMessageBox.Yes:
            try:
                db = con.connect(host="localhost", user="root",
                                password="", db="testproject1")
                cursor = db.cursor()
                query = "Select selled_drugs_user_info.id, selled_drugs_user_info.user_name, selled_drugs_user_info.user_phone, selled_drugs_user_info.user_address, selled_drugs_user_info.ordered_datetime, selled_drugs.drug_name, selled_drugs.drug_company, selled_drugs.price, selled_drugs.quantity, selled_drugs.total_price from selled_drugs INNER JOIN selled_drugs_user_info ON selled_drugs.ref_id = selled_drugs_user_info.id Where selled_drugs_user_info.id = '"+user_id+"'"
                cursor.execute(query.format(self.ui.invoice_table))
                result = cursor.fetchall()
                self.inv.createInvoice(result)
                self.inv.dumpInvoice(result)
                db.close()

            except Exception as e:
                print(e)
                print("Check your Server!")
                db.close()
        else:
            return

    def user_buy_drug_btn_clicked(self):    
        user_name = self.ui.user_name_lineEdit.text()
        user_phone = self.ui.user_phone_lineEdit.text()
        user_address = self.ui.user_address_lineEdit.text()
        user_drug_price = self.ui.user_drug_price_lineEdit.text()
        user_drug_name = self.ui.user_drug_name_combobox.currentText()
        user_quantity = self.ui.user_drug_quantity_combobox.currentText()
        user_company = self.ui.user_drug_company_comboBox.currentText()
        date_time = datetime.datetime.now()
        ordered_datetime = date_time.strftime("%m/%d/%Y, %H:%M:%S")
        print(ordered_datetime)
          
        if len(user_name) != 0 or len(user_phone) != 0 or len(user_address) != 0 or len(user_drug_price) != 0 or len(user_quantity) != 0 or len(user_company) != 0 or len(user_drug_name) != 0:
            pass
        else:
            QMessageBox.information(self, "Updating", "Empty Upadate!")
            return

        try: 
            db = con.connect(host="localhost", user="root", password="", db="testproject1")
            cursor = db.cursor()
            
            isEmpty = "select COUNT(id) from selled_drugs_user_info"
            reset_primary_key1 = "alter table selled_drugs_user_info AUTO_INCREMENT=1"
            reset_primary_key2 = "truncate table selled_drugs_user_info"
            cursor.execute(isEmpty.format(self.ui.users_drugs_list_table))
            isEmpty_result = cursor.fetchall()
            print("Selled Users Info: ", isEmpty_result)

            if isEmpty_result[0][0] == 0:
                cursor.execute(reset_primary_key1)
                cursor.execute(reset_primary_key2)
                db.commit()
            
            selled_drugs_user_info_query = "Insert into selled_drugs_user_info (user_name, user_phone, user_address, ordered_datetime) values ('" +user_name+"', '" +user_phone+"', '"+user_address+"', '"+ordered_datetime+"')"
            cursor.execute(selled_drugs_user_info_query)
            selled_drugs_query = "Insert Into selled_drugs (ref_id, drug_name, drug_company, price, quantity, total_price) Select * from user_cart"
            cursor.execute(selled_drugs_query)
            db.commit()
            QMessageBox.information(self, "Order", "Drug Ordered Successfully")
            print("Drug Ordered Successfully")
            self.user_drugs_refresh_btn_clicked()
            db.close()
        except Exception as e:
            print(e)
            print("Order Interrupted!")
            db.close()

    def supplier_search_btn_clicked(self):        
        supp_name = self.ui.supp_name_lineEdit.text()
        supp_phone = self.ui.supp_phone_lineEdit.text()
        supp_email = self.ui.supp_email_lineEdit.text()
        supp_address = self.ui.supp_address_lineEdit.text()
        supp_id_number = self.ui.id_number_lineEdit.text()
        supp_drug_company = self.ui.supp_drrug_company_lineEdit.text()
        supp_id_proof = self.ui.supp_id_proof_combobox.currentText()

        if len(supp_name) != 0 or len(supp_phone) != 0 or len(supp_email) != 0 or len(supp_address) != 0 or len(supp_id_number) != 0 or len(supp_drug_company) != 0 or len(supp_id_proof) != 0:
            pass
        else:
            QMessageBox.information(self, "Updating", "Empty Upadate!")
            return        
        search_querry = "Select * from suppliers Where supp_name like '"+supp_name+"' OR supp_phone like '"+supp_phone+"' OR supp_email like '" + supp_email +"' OR supp_address like '"+supp_address+"' OR supp_idnumber like '"+supp_id_number+"' OR drug_company like '"+supp_drug_company+"' "
        self.populate_suppliers_table(search_querry)
        
        

    def add_supplier_btn_clicked(self):
        supp_name = self.ui.supp_name_lineEdit.text()
        supp_phone = self.ui.supp_phone_lineEdit.text()
        supp_email = self.ui.supp_email_lineEdit.text()
        supp_address = self.ui.supp_address_lineEdit.text()
        supp_id_number = self.ui.id_number_lineEdit.text()
        supp_drug_company = self.ui.supp_drrug_company_lineEdit.text()
        supp_id_proof = self.ui.supp_id_proof_combobox.currentText()

        if len(supp_name) != 0 or len(supp_phone) != 0 or len(supp_email) != 0 or len(supp_address) != 0 or len(supp_id_number) != 0 or len(supp_drug_company) != 0 or len(supp_id_proof) != 0:
            pass
        else:
            QMessageBox.information(self, "Updating", "Empty Upadate!")
            return

        try: 
            db = con.connect(host="localhost", user="root", password="", db="testproject1")
            supplier_query = "insert into suppliers (supp_name , supp_phone , supp_email, supp_address, supp_idproof, supp_idnumber, drug_company) values ('" +supp_name +"', '"+supp_phone +"', '"+supp_email+"', '" + supp_address + "', '" +supp_id_proof+"', '" + supp_id_number + "', '"+supp_drug_company+"') "
            cursor = db.cursor()
            cursor.execute(supplier_query)
            db.commit()
            QMessageBox.information(self, "Suppliers", "Supplier Added Successfully")
            print("Supplier Added Successfully")
            db.close()
        except Exception as e:
            print(e)
            QMessageBox.information(self, "Suppliers", "Supplier Adding Drug!")
            print("Supplier Adding Drug!")
            db.close()
        self.populate_suppliers_table(self.populate_suppliers_query)

    def supp_id_proof_combobox_changed(self, index):
        if index == 0:
            self.ui.id_number_lineEdit.setPlaceholderText("XXXX XXXX XXXX")
            self.ui.id_number_lineEdit.setMaxLength(12)
            self.ui.id_number_lineEdit.setValidator(self.only_int)
        if index == 1:
            self.ui.id_number_lineEdit.setPlaceholderText("ABCDE1234Z")
            self.ui.id_number_lineEdit.setMaxLength(10)
            self.ui.id_number_lineEdit.setValidator(self.only_int_str)
        if index == 2:
            self.ui.id_number_lineEdit.setPlaceholderText("ABCDE12345")
            self.ui.id_number_lineEdit.setMaxLength(10)
            self.ui.id_number_lineEdit.setValidator(self.only_int_str)
        if index == 3:
            self.ui.id_number_lineEdit.setPlaceholderText("XXXXXXXXXXXXXXX")
            self.ui.id_number_lineEdit.setMaxLength(15)
            self.ui.id_number_lineEdit.setValidator(self.only_int)

    def user_drug_company_changed(self):
        user_drug_company = self.ui.user_drug_company_comboBox.currentText()
        self.ui.user_drug_name_combobox.clear()
        try:
            db = con.connect(host="localhost", user="root", password="", db="testproject1")
            cursor = db.cursor()
            query = "Select DISTINCT name from drugs where company = '"+user_drug_company+"' and quantity > 0"
            cursor.execute(query.format(self.ui.users_drugs_list_table))
            result = cursor.fetchall()
            for index, item in enumerate(result):
                self.ui.user_drug_name_combobox.addItem(item[0])
            db.close()
        except Exception as e:
            print(e)
            print("Check your Server!")
            db.close()

    def user_drug_name_changed(self):
        user_drug_name = self.ui.user_drug_name_combobox.currentText()
        user_drug_company = self.ui.user_drug_company_comboBox.currentText()
        try:
            db = con.connect(host="localhost", user="root", password="", db="testproject1")
            cursor = db.cursor()
            query = "Select price from drugs where name = '"+user_drug_name+"' and company = '"+user_drug_company+"'"
            cursor.execute(query.format(self.ui.users_drugs_list_table))
            result = cursor.fetchall()
            print(result[0][0])
            self.ui.user_drug_price_lineEdit.setText(result[0][0])
            db.close()
        except Exception as e:
            print(e)
            # print("Check your Server!")
            db.close()
        
    def populate_suppliers_table(self, query):
        try:
            db = con.connect(host="localhost", user="root",
                             password="", db="testproject1")
            cursor = db.cursor()
            # query = "Select * from suppliers"
            cursor.execute(query.format(self.ui.suppliers_table))
            result = cursor.fetchall()

            self.ui.suppliers_table.setRowCount(0)
            self.ui.suppliers_table.setColumnCount(7)
            self.ui.suppliers_table.setHorizontalHeaderLabels(["Name", "Phone", "Email", "Address", "ID Proof", "ID Number", "Company"])
            self.ui.suppliers_table.setColumnWidth(0, 105)
            self.ui.suppliers_table.setColumnWidth(1, 105)
            self.ui.suppliers_table.setColumnWidth(2, 105)
            self.ui.suppliers_table.setColumnWidth(3, 105)
            self.ui.suppliers_table.setColumnWidth(4, 105)
            self.ui.suppliers_table.setColumnWidth(5, 105)
            self.ui.suppliers_table.setColumnWidth(6, 105)

            for row, row_data in enumerate(result):
                self.ui.suppliers_table.insertRow(row)
                for column, data in enumerate(row_data):
                    self.ui.suppliers_table.setItem(
                        row, column, QtWidgets.QTableWidgetItem(str(data)))
            db.close()
        except Exception as e:
            print(e)
            print("Check your Server!")
            db.close()
        
    def populate_users_table(self):
        try:
            db = con.connect(host="localhost", user="root",
                             password="", db="testproject1")
            cursor = db.cursor()
            query = "Select drug_name , drug_company, price, quantity, total_price from user_cart"
            total_price_query = "Select SUM(total_price) from user_cart"
            cursor.execute(query.format(self.ui.users_drugs_list_table))
            result = cursor.fetchall()

            cursor.execute(total_price_query.format(self.ui.users_drugs_list_table))
            sum_result = cursor.fetchall()
            print(sum_result[0][0])
            if sum_result[0][0] != None:
                self.ui.user_drug_total_price_lineEdit.setText('₹' + str(sum_result[0][0]))
            else:
                self.ui.user_drug_total_price_lineEdit.setText('₹')

            self.ui.users_drugs_list_table.setRowCount(0)
            self.ui.users_drugs_list_table.setColumnCount(5)
            self.ui.users_drugs_list_table.setHorizontalHeaderLabels(["Name", "Company", "Price", "Quantity", "Total Price"])
            self.ui.users_drugs_list_table.setColumnWidth(0, 148)
            self.ui.users_drugs_list_table.setColumnWidth(1, 148)
            self.ui.users_drugs_list_table.setColumnWidth(2, 148)
            self.ui.users_drugs_list_table.setColumnWidth(3, 148)
            self.ui.users_drugs_list_table.setColumnWidth(4, 148)

            for row, row_data in enumerate(result):
                self.ui.users_drugs_list_table.insertRow(row)
                for column, data in enumerate(row_data):
                    self.ui.users_drugs_list_table.setItem(
                        row, column, QtWidgets.QTableWidgetItem(str(data)))
            db.close()
        except Exception as e:
            print(e)
            print("Check your Server!")
            db.close()

    def text_changed(self):
        if self.ui.drug_manf_lineEdit.cursorPosition() == 2 or self.ui.drug_manf_lineEdit.cursorPosition() == 5:
            text = self.ui.drug_manf_lineEdit.text()
            self.ui.drug_manf_lineEdit.setText(text + "/")

    def switch_to_ivoice_page(self, event):
        global status_flag 
        if status_flag == 1:
            self.ui.stackedWidget.setCurrentIndex(2)
            self.invoice_table()
        else:
            QMessageBox.information(self, "Admin", "This is for Admin!")

    def switch_to_stock_page(self, event):
        global status_flag 
        if status_flag == 1:
            self.ui.stackedWidget.setCurrentIndex(4)
            self.ui.drug_id_lineEdit.setFocus()
            current_date = datetime.date.today()
            current_date_string = current_date.strftime('%d/%m/%Y')
            self.ui.drug_manf_lineEdit.setText(current_date_string)
            self.ui.drug_exp_lineEdit.setText(current_date_string)
            self.populate_drugs_table(self.query)
            self.populate_drugs_company_comboBox()
        else:
            QMessageBox.information(self, "Admin", "This is for Admin!")
        
    def populate_drugs_company_comboBox(self):
        self.ui.company_comboBox.clear()
        try: 
            db = con.connect(host="localhost", user="root", password="", db="testproject1")
            supp_company = "Select DISTINCT drug_company from suppliers"
            cursor = db.cursor()
            cursor.execute(supp_company.format(self.ui.suppliers_table))
            result = cursor.fetchall()
            print(result)
            for index, item in enumerate(result):
                self.ui.company_comboBox.addItem(item[0])
            print("Company Added Successfully")
            db.close()
        except Exception as e:
            print(e)
            QMessageBox.information(self, "Drugs", "Error Adding Drug!")
            print("Error Adding Drug!")
            db.close()

    def suppliers_refresh_btn_clicked(self):
        self.populate_suppliers_table(self.populate_suppliers_query)

    def switch_to_supplier_page(self, event):
        global status_flag 
        if status_flag == 1:
            self.ui.stackedWidget.setCurrentIndex(1)
            self.populate_suppliers_table(self.populate_suppliers_query)
        else:
            QMessageBox.information(self, "Admin", "This is for Admin!")

    def home_label_clicked(self, event):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.populate_user_drug_company_comboBox()
        
    def populate_user_drug_company_comboBox(self):
        self.ui.user_drug_company_comboBox.clear()
        try: 
            db = con.connect(host="localhost", user="root", password="", db="testproject1")
            supp_company = "Select DISTINCT company from drugs"
            cursor = db.cursor()
            cursor.execute(supp_company.format(self.ui.users_drugs_list_table))
            result = cursor.fetchall()
            print(result)
            for index, item in enumerate(result):
                self.ui.user_drug_company_comboBox.addItem(item[0])
            print("Company Added Successfully")
            db.close()
        except Exception as e:
            print(e)
            QMessageBox.information(self, "Drugs", "Error Adding Drug!")
            print("Error Adding Drug!")
            db.close()


    def delete_drug_btn_clicked(self):
        drug_id = self.ui.drug_id_lineEdit.text()

        if len(drug_id) != 0:
            pass
        else:
            QMessageBox.information(self, "Deleting", "Empty Delete!")
            return

        try:
            db = con.connect(host="localhost", user="root",
                             password="", db="testproject1")
            delete_query = "Delete from drugs Where drug_id = '"+drug_id+"'"
            cursor = db.cursor()
            cursor.execute(delete_query)
            db.commit()
            print("Drug Deleted Successfully")
            db.close()
            self.refresh_btn_clicked()
        except Exception as e:
            print(e)
            QMessageBox.information(self, "Drugs", "Error Deleting Drug!")
            print("Error Deleting Drug!")
            db.close()

    def user_drugs_refresh_btn_clicked(self):
        self.populate_user_drug_company_comboBox()
        self.user_drug_company_changed()
        try:
            db = con.connect(host="localhost", user="root", password="", db="testproject1")
            delete_uerry = "Delete from user_cart"
            cursor = db.cursor()
            cursor.execute(delete_uerry)
            db.commit()
            print("Drug Added Successfully")
            db.close()
        except Exception as e:
            print(e)
            QMessageBox.information(self, "Drugs", "Error Updating Drug!")
            print("Error Adding Drug!")
            db.close()
        self.populate_users_table()

    def refresh_btn_clicked(self):
        self.populate_drugs_table(self.query)
        self.ui.drug_id_lineEdit.setText("")
        self.ui.drug_name_lineEdit.setText("")
        self.ui.drug_price_lineEdit.setText("")
        self.ui.drug_quantity_lineEdit.setText("")
        current_date = datetime.date.today()
        current_date_string = current_date.strftime('%m/%d/%Y')
        self.ui.drug_manf_lineEdit.setText(current_date_string)
        self.ui.drug_exp_lineEdit.setText(current_date_string)
        self.populate_drugs_company_comboBox()

    def drugs_table_item_clicked(self):
        items_list = self.ui.drugs_table.selectedItems()
        print(items_list[1].text())
        self.ui.drug_id_lineEdit.setText(items_list[1].text())
        self.ui.drug_name_lineEdit.setText(items_list[2].text())
        self.ui.drug_price_lineEdit.setText(items_list[3].text())
        self.ui.drug_quantity_lineEdit.setText(items_list[4].text())
        self.ui.drug_manf_lineEdit.setText(items_list[5].text())
        self.ui.drug_exp_lineEdit.setText(items_list[6].text())
        self.ui.company_comboBox.clear()
        self.ui.company_comboBox.addItem(items_list[7].text())

    def update_drug_btn_clicked(self):
        drug_id = self.ui.drug_id_lineEdit.text()
        name = self.ui.drug_name_lineEdit.text()
        price = self.ui.drug_price_lineEdit.text()
        quantity = self.ui.drug_quantity_lineEdit.text()
        manf_date = self.ui.drug_manf_lineEdit.text()
        exp_date = self.ui.drug_exp_lineEdit.text()
        company_name = self.ui.company_comboBox.currentText()

        if len(drug_id) != 0 or len(name) != 0 or len(price) != 0 or len(quantity) != 0 or len(manf_date) != 0 or len(exp_date) != 0 or len(company_name) != 0:
            pass
        else:
            QMessageBox.information(self, "Updating", "Empty Upadate!")
            return

        try:
            db = con.connect(host="localhost", user="root",
                             password="", db="testproject1")
            registerQuerry = "Update drugs Set name = '"+name+"', price = '"+price+"', quantity = '" + quantity + "', manf_date = '" + \
                manf_date+"', exp_date = '" + exp_date + "', company = '" + \
                company_name+"' where drug_id = '"+drug_id+"' "
            cursor = db.cursor()
            cursor.execute(registerQuerry)
            db.commit()
            QMessageBox.information(self, "Drugs", "Drug Updated Successfully")
            print("Drug Added Successfully")
            db.close()
        except Exception as e:
            print(e)
            QMessageBox.information(self, "Drugs", "Error Updating Drug!")
            print("Error Adding Drug!")
            db.close()
        self.populate_drugs_table(self.query)

    def search_drug_btn_clicked(self):
        drug_id = self.ui.drug_id_lineEdit.text()
        name = self.ui.drug_name_lineEdit.text()
        price = self.ui.drug_price_lineEdit.text()
        quantity = self.ui.drug_quantity_lineEdit.text()
        manf_date = self.ui.drug_manf_lineEdit.text()
        exp_date = self.ui.drug_exp_lineEdit.text()
        company_name = self.ui.company_comboBox.currentText()

        if len(drug_id) != 0 or len(name) != 0 or len(price) != 0 or len(quantity) != 0 or len(manf_date) != 0 or len(exp_date) != 0 or len(company_name) != 0:
            pass
        else:
            QMessageBox.information(self, "Searching", "Empty Search!")
            return

        registerQuerry = "Select * from drugs Where name like '"+name+"' OR price like '"+price+"' OR quantity like '" + quantity + \
            "' OR manf_date like '"+manf_date+"' OR exp_date like '" + exp_date + \
            "' OR company like '"+company_name+"' OR drug_id like '"+drug_id+"' "
        self.populate_drugs_table(registerQuerry)

    def add_users_drug_btn_clicked(self):
        drug_name = self.ui.user_drug_name_combobox.currentText()
        new_quatity = self.ui.user_drug_quantity_combobox.currentText()
        drug_price = self.ui.user_drug_price_lineEdit.text()
        company_name = self.ui.user_drug_company_comboBox.currentText()
        total_price = str(int(drug_price)*int(new_quatity))
        ref_id = 0
        updated_quantity = 0
        quantity = 0
        quantity_result = 0

        if len(drug_name) != 0 and len(new_quatity) != 0 and len(company_name) != 0:
            pass
        else:
            QMessageBox.information(self, "SignUp", "Each Field is Mandatory!")
            return

        try: 
            db = con.connect(host="localhost", user="root", password="", db="testproject1")
            cursor = db.cursor()
            
            quantity_query = "select quantity from drugs where company = '"+company_name+"' and name = '"+drug_name+"'"
            
            cursor.execute(quantity_query.format(self.ui.users_drugs_list_table))
            quantity_result = cursor.fetchall()
            print(quantity_result)
            quantity = int(quantity_result[0][0])           
            updated_quantity = str((quantity) - int(new_quatity))     
            isEmpty = "select COUNT(id) ,MAX(ref_id) from selled_drugs"
            reset_primary_key1 = "alter table selled_drugs AUTO_INCREMENT=1"
            reset_primary_key2 = "truncate table selled_drugs"
            cursor.execute(isEmpty.format(self.ui.users_drugs_list_table))
            isEmpty_result = cursor.fetchall()
            registerQuerry = "Update drugs set quantity = '"+updated_quantity+"'"
            cursor.execute(registerQuerry)
            db.commit()
            print(isEmpty_result)
            if isEmpty_result[0][0] == 0:
                ref_id = str(1);
                cursor.execute(reset_primary_key1)
                cursor.execute(reset_primary_key2)
                db.commit()
                print(isEmpty_result[0][0])
                print("ref_id", ref_id)
            else:
                ref_id = str(isEmpty_result[0][1] + 1)
                print(isEmpty_result[0][1])
                print("ref_id",ref_id)

            registerQuerry = "insert into user_cart (ref_id, drug_name , drug_company, price, quantity, total_price) values ('" +ref_id+"', '" +drug_name+"', '"+company_name+"', '"+drug_price+"', '" +new_quatity+ "', '"+total_price+"')"
            cursor.execute(registerQuerry)
            db.commit()
            print("Drug Added Successfully")
            db.close()
            self.populate_users_table()
        except Exception as e:
            print(e)
            QMessageBox.information(self, "Drugs", "Error Adding Drug!")
            print("Error Adding Drug!")
            db.close()

    def add_drug_btn_clicked(self):
        drug_id = self.ui.drug_id_lineEdit.text()
        name = self.ui.drug_name_lineEdit.text()
        price = self.ui.drug_price_lineEdit.text()
        new_quatity = self.ui.drug_quantity_lineEdit.text()
        manf_date = self.ui.drug_manf_lineEdit.text()
        exp_date = self.ui.drug_exp_lineEdit.text()
        company_name = self.ui.company_comboBox.currentText()
        quantity = 0
        quantity_result = 0

        if len(drug_id) != 0 and len(name) != 0 and len(price) != 0 and len(new_quatity) != 0 and len(manf_date) != 0 and len(exp_date) != 0 and len(company_name) != 0:
            pass
        else:
            QMessageBox.information(self, "SignUp", "Each Field is Mandatory!")
            return

        try: 
            db = con.connect(host="localhost", user="root", password="", db="testproject1")
            search_Querry = "Select * from drugs Where drug_id like '"+drug_id+"' OR name like '"+name+"' OR company like '"+company_name+"'"
            cursor = db.cursor()
            cursor.execute(search_Querry.format(self.ui.invoice_table))
            result = cursor.fetchall()
            print(quantity_result)
            if result != 0:
                Querry = "Select quantity from drugs where drug_id = '"+drug_id+"'"
                cursor.execute(Querry.format(self.ui.invoice_table))
                quantity_result = cursor.fetchall()
                print(quantity_result)
                quantity = int(quantity_result[0][0])
                updated_quantity = str(quantity + int(new_quatity))
                print(updated_quantity)
                registerQuerry = "Update drugs set quantity = '"+updated_quantity+"' where drug_id = '"+drug_id+"'"
                cursor.execute(registerQuerry)
                db.commit()
                self.search_drug_btn_clicked()
                db.close()
                return

        except Exception as e:
            print(e)
            QMessageBox.information(self, "Drugs", "Error Adding Drug!")
            print("Error Adding Drug!")
            db.close()

        try: 
            db = con.connect(host="localhost", user="root", password="", db="testproject1")
            registerQuerry = "insert into drugs (drug_id, name, price, quantity, manf_date, exp_date, company) values ('" +drug_id+"', '"+name+"', '"+price+"', '" + new_quatity + "', '" +manf_date+"', '" + exp_date + "', '"+company_name+"') "
            cursor = db.cursor()
            cursor.execute(registerQuerry)
            db.commit()
            QMessageBox.information(self, "Drugs", "Drug Added Successfully")
            print("Drug Added Successfully")
            db.close()
        except Exception as e:
            print(e)
            QMessageBox.information(self, "Drugs", "Error Adding Drug!")
            print("Error Adding Drug!")
            db.close()
        self.populate_drugs_table(self.query)

    def invoice_table(self):
        try:
            db = con.connect(host="localhost", user="root",
                             password="", db="testproject1")
            cursor = db.cursor()
            query = "Select selled_drugs_user_info.id, selled_drugs_user_info.user_name, selled_drugs_user_info.user_phone, selled_drugs_user_info.user_address, selled_drugs_user_info.ordered_datetime, selled_drugs.drug_name, selled_drugs.drug_company, selled_drugs.price, selled_drugs.quantity, selled_drugs.total_price from selled_drugs INNER JOIN selled_drugs_user_info ON selled_drugs.ref_id = selled_drugs_user_info.id"
            cursor.execute(query.format(self.ui.invoice_table))
            result = cursor.fetchall()
            print(result)
            
            # self.inv.createInvoice(result)
            # self.inv.dumpInvoice(result)

            self.ui.invoice_table.setRowCount(0)
            self.ui.invoice_table.setColumnCount(10)
            self.ui.invoice_table.setHorizontalHeaderLabels(
                ["id", "Name", "Phone", "Address", "Datetime", "Drug", "Company", "Price", "Quan\ntity", "Total"])
            self.ui.invoice_table.setColumnWidth(0, 40)
            self.ui.invoice_table.setColumnWidth(1, 135)
            self.ui.invoice_table.setColumnWidth(2, 74)
            self.ui.invoice_table.setColumnWidth(3, 120)
            self.ui.invoice_table.setColumnWidth(4, 120)
            self.ui.invoice_table.setColumnWidth(5, 74)
            self.ui.invoice_table.setColumnWidth(6, 74)
            self.ui.invoice_table.setColumnWidth(7, 40)
            self.ui.invoice_table.setColumnWidth(8, 37)
            self.ui.invoice_table.setColumnWidth(9, 40)

            for row, row_data in enumerate(result):
                self.ui.invoice_table.insertRow(row)
                for column, data in enumerate(row_data):
                    self.ui.invoice_table.setItem(
                        row, column, QtWidgets.QTableWidgetItem(str(data)))
            db.close()
        except Exception as e:
            print(e)
            print("Check your Server!")
            db.close()

    def populate_drugs_table(self, query):
        try:
            db = con.connect(host="localhost", user="root",
                             password="", db="testproject1")
            cursor = db.cursor()
            cursor.execute(query.format(self.ui.drugs_table))
            result = cursor.fetchall()

            self.ui.drugs_table.setRowCount(0)
            self.ui.drugs_table.setColumnCount(8)
            self.ui.drugs_table.setHorizontalHeaderLabels(
                ["id", "Drug_id", "Name", "Price", "Quantity", "Manf", "Exp", "Company"])
            self.ui.drugs_table.setColumnWidth(0, 50)
            self.ui.drugs_table.setColumnWidth(1, 80)
            self.ui.drugs_table.setColumnWidth(2, 170)
            self.ui.drugs_table.setColumnWidth(3, 70)
            self.ui.drugs_table.setColumnWidth(4, 90)
            self.ui.drugs_table.setColumnWidth(5, 70)
            self.ui.drugs_table.setColumnWidth(6, 70)
            self.ui.drugs_table.setColumnWidth(7, 95)

            for row, row_data in enumerate(result):
                self.ui.drugs_table.insertRow(row)
                for column, data in enumerate(row_data):
                    self.ui.drugs_table.setItem(
                        row, column, QtWidgets.QTableWidgetItem(str(data)))
            db.close()
        except Exception as e:
            print(e)
            print("Check your Server!")
            db.close()

    def clicked_item(self):
        items_list = self.ui.users_table.selectedItems()
        user_id = items_list[0].text()
        print(user_id)

        warning_msg = QMessageBox()
        warning_msg.setIcon(QMessageBox.Question)
        warning_msg.setText("Do Want Allow User?")
        warning_msg.setWindowTitle("Question")
        warning_msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        if warning_msg.exec() == QMessageBox.Yes:
            try:
                db = con.connect(host="localhost", user="root",
                                 password="", db="testproject1")
                updateUserStatus = "Update ManageUsers Set Status = 'Allowed' Where id = '" + user_id + "'"
                cursor = db.cursor()
                cursor.execute(updateUserStatus)
                db.commit()
                print("Status Changed Successfully")
                db.close()
                self.populate_user_table()
            except Exception as e:
                print(e)
                print("Error Changing Status!")
                db.close()
        else:
            try:
                db = con.connect(host="localhost", user="root", password="", db="testproject1")
                updateUserStatus = "Update ManageUsers Set Status = 'Not-Allowed' Where id = '" + user_id + "'"
                cursor = db.cursor()
                cursor.execute(updateUserStatus)
                db.commit()
                print("Status Changed Successfully")
                db.close()
                self.populate_user_table()
            except Exception as e:
                print(e)
                print("Error Changing Status!")
                db.close()

    def exit_label_clicked(self, event):
        self.user_drugs_refresh_btn_clicked()
        sys.exit()

    def switch_to_admin_page(self, event):
        global status_flag 
        if status_flag == 1:
            self.ui.stackedWidget.setCurrentIndex(3)
            self.populate_user_table()
        else:
            QMessageBox.information(self, "Admin", "This is for Admin!")

    def populate_user_table(self):
        try:
            db = con.connect(host="localhost", user="root",
                             password="", db="testproject1")
            query = "select id, Name, Age, Gender, Phone, Email, Username, Password from manageusers"
            cursor = db.cursor()
            cursor.execute(query.format(self.ui.users_table))
            result = cursor.fetchall()

            self.ui.users_table.setRowCount(0)
            self.ui.users_table.setColumnCount(8)
            self.ui.users_table.setHorizontalHeaderLabels(
                ["id", "Name", "Age", "Gender", "Phone", "Email", "Username", "Password"])
            self.ui.users_table.setColumnWidth(0, 42)
            self.ui.users_table.setColumnWidth(1, 173)
            self.ui.users_table.setColumnWidth(2, 40)
            self.ui.users_table.setColumnWidth(3, 57)
            self.ui.users_table.setColumnWidth(4, 75)
            self.ui.users_table.setColumnWidth(5, 188)
            self.ui.users_table.setColumnWidth(6, 86)
            self.ui.users_table.setColumnWidth(7, 86)
            # self.ui.users_table.setColumnWidth(8, 82)

            print(result)
            # print(enumerate(result))
            for row, row_data in enumerate(result):
                self.ui.users_table.insertRow(row)

                for column, data in enumerate(row_data):
                    self.ui.users_table.setItem(
                        row, column, QtWidgets.QTableWidgetItem(str(data)))
            db.close()
        except Exception as e:
            print(e)
            print("Check your Server!")
            db.close()


class Main:
    def __init__(self):
        super(Main, self).__init__()

    def currentIndex(self, widget, index):
        widget.setCurrentIndex(index)
        if index == 0:
            widget.setFixedHeight(600)
            widget.setFixedWidth(500)
        elif index == 1:
            widget.setFixedHeight(750)
            widget.setFixedWidth(1000)


# App Execution
app = QApplication([])
widget = QtWidgets.QStackedWidget()
login_widget = LoginPage()
main_window_widget = MainWindow()
signup_widget = SignUpPage()
main = Main()
widget.addWidget(login_widget)
widget.addWidget(main_window_widget)
widget.addWidget(signup_widget)
widget.setFixedHeight(500)
widget.setFixedWidth(410)
widget.setWindowFlags(widget.windowFlags() | Qt.FramelessWindowHint)

# Frame Center (Co-ordinates)
screen_size = QScreen.availableGeometry(QApplication.primaryScreen())
x = (screen_size.width() - 410)/2
y = (screen_size.height() - 500)/2 - 15
widget.move(x, y)
widget.show()

status_flag = 1

sys.exit(app.exec())