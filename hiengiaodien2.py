# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 18:32:59 2025

@author: ThanhHa
"""

import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
#from xuly import *
from apple_moi import *

class MainWindow:
    def __init__(self):
        self.main_win=QWidget()
        self.ui=Ui_Quanlydanhba()
        self.ui.setupUi(self.main_win)
        self.lienketnutlenh()
    def show(self):
        self.main_win.show()
    def lienketnutlenh(self):
        self.ui.tim_kiem.clicked.connect(self.search_contact)
        self.ui.them.clicked.connect(self.addContact)
        self.ui.hien_thi.clicked.connect(self.showListContacts)
        self.ui.xoa.clicked.connect(self.deleteContact)


    def addContact(self):
        name = self.ui.lneten.text().strip()
        try:
            sdt = int(self.ui.lnesdt.text().strip())
        except ValueError:
            QMessageBox.warning(self.main_win, "Lỗi", "Vui lòng nhập đúng số!")
            return
        email =self.ui.lneemail.text().strip()
        # Validate input
        if not name or not sdt:
            QMessageBox.warning(self.main_win, "Lỗi", "Vui lòng nhập đầy đủ tên và số!")
            return



        thongtin = f"{name}    {sdt}     {email}"

        contacts = self.read_contacts()  # Read existing contacts
        contacts.append(thongtin + "\n")  # Add new contact
        self.write_contacts(contacts)  # Save updated list

        self.ui.lneemail.clear()
        self.ui.lnesdt.clear()
        self.ui.lneten.clear()

        self.ui.tb_list_contacts.clear()
        self.ui.tb_list_contacts.append(thongtin)


    def read_contacts(self):
        try:
            with open("list_contacts.txt", "r", encoding="utf-8") as f:
                return f.readlines()
        except FileNotFoundError:
            return []

    def write_contacts(self, contacts):
        try:
            with open("list_contacts.txt", "w", encoding="utf-8") as f:
                for contact in contacts:
                    # Ensure each contact ends with a newline
                    if not contact.endswith("\n"):
                        contact += "\n"
                    f.write(contact)
            print("Contacts saved successfully.")  # Optional debug line
        except Exception as e:
            print(f"Error writing contacts: {e}")

    def search_contact(self):
        name = self.ui.lneten.text().strip().lower()
        contacts = self.read_contacts()

        self.ui.tb_list_contacts.clear()

        results = [c for c in contacts if name in c.lower()]

        if results:
            for contact in results:
                self.ui.tb_list_contacts.append(contact)
        else:
            self.ui.tb_list_contacts.setText("Không tìm thấy liên lạc.")

    def showListContacts(self):
        contacts = self.read_contacts()
        self.ui.tb_list_contacts.clear()
        for contact in contacts:
            self.ui.tb_list_contacts.append(contact)

    def deleteContact(self):
        name = self.ui.lneten.text().strip().lower()
        sdt = int(self.ui.lnesdt.text().strip().lower())
        contacts = self.read_contacts()
        #cần try/except không?
        if not name and sdt:
            QMessageBox.warning(self.main_win, "Lỗi", "Vui lòng nhập liên hệ!")
            return

        remaining_contacts = [c for c in contacts if name not in c.lower()]

        if len(remaining_contacts) == len(contacts):
            self.ui.tb_list_contacts.setText("Không tìm thấy liên lạc để xóa.")
            return

        self.write_contacts(remaining_contacts)

        self.ui.tb_list_contacts.setText(f"Đã xóa liên lạc có chứa '{name}'.")


if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    app.exec()