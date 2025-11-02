# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 18:32:59 2025

@author: ThanhHa
"""

import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget
#from xuly import *
from apple import *

class MainWindow:
    def __init__(self):
        self.main_win=QWidget()
        self.ui=Ui_Quanlydanhba()
        self.ui.setupUi(self.main_win)
        self.lienketnutlenh()
        self.ui.grbox.hide() #ẩn groupbox khi khởi tạo
        self.ui.danhba.hide()
        self.ui.pbcancel.hide()
    def show(self):
        self.main_win.show()
    def lienketnutlenh(self):
        self.ui.pbtaolienhe.clicked.connect(self.xulynoibo)
        self.ui.pbthem.clicked.connect(self.luudanhba)
        self.ui.pbcancel.clicked.connect(self.cancel)
    def xulynoibo(self):
        self.ui.grbox.show() #bấm vào dấu cộng thì sẽ hiện ra màn hình
        self.ui.pbcancel.show()
    def luudanhba(self):
        ten=self.ui.lneten.text()
        sdt=self.ui.lnesdt.text()
        email=self.ui.lneemail.text()
        thongtin=f"Tên: {ten} Số điện thoại: {sdt}    Email: {email}"
        #tieude=f"Tên                Số điện thoại               Email" #căn lề cho tiêu đề và thông tin 
        #self.ui.danhba.addItem(tieude)
        self.ui.danhba.addItem(thongtin) #thêm thông tin vào listqwidget danh bạ
        self.ui.danhba.show()
        self.ui.lneemail.clear()
        self.ui.lnesdt.clear()
        self.ui.lneten.clear()
    def cancel(self):
        self.ui.grbox.close() #cần sửa lại nếu muốn có phần cancel cho phần tạo liên hệ
        self.ui.pbcancel.hide()

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    app.exec()