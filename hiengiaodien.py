# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 18:32:59 2025

@author: ThanhHa
"""
hello

import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget
#from xuly import *
from new_apple import *

class MainWindow:
    def __init__(self):
        self.main_win=QWidget()
        self.ui=Ui_Quanlydanhba()
        self.ui.setupUi(self.main_win)
        self.lienketnutlenh()
        self.ui.grbox.hide() #ẩn groupbox khi khởi tạo
        # self.ui.danhba.hide()
        self.ui.pbcancel.hide()
    def show(self):
        self.main_win.show()
    def lienketnutlenh(self):
        self.ui.tim_kiem.clicked.connect(self.search_contact)
        self.ui.pbthem.clicked.connect(self.luudanhba)
        self.ui.them.clicked.connect(self.xulynoibo)
        self.ui.hien_thi.clicked.connect(self.showListContacts)
        self.ui.xoa.clicked.connect(self.deleteContact)

    def xulynoibo(self):
        self.ui.grbox.show() #bấm vào dấu cộng thì sẽ hiện ra màn hình
        self.ui.pbcancel.show()
    def luudanhba(self):
        ten=self.ui.lneten.text()
        sdt=self.ui.lnesdt.text()
        email=self.ui.lneemail.text()
        thongtin=f"{ten}    {sdt}    {email}"
        tieude=f"Tên                Số điện thoại               Email" #căn lề cho tiêu đề và thông tin 
        self.ui.danhba.addItem(tieude)
        self.ui.danhba.addItem(thongtin) #thêm thông tin vào listqwidget danh bạ
        self.ui.danhba.show()
        
        self.ui.lneemail.clear()
        self.ui.lnesdt.clear()
        self.ui.lneten.clear()

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
        contacts = self.read_contacts()

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
