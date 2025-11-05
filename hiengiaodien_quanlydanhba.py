import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem, QHeaderView
# QmessageBox:để dùng thư viện hiện thông báo
# QTableWidgetItem:dùng thư viện để gán giá trị cho từng cột và hàng trong bảng
# Qheaderview: dùng để điều chỉnh cột của bảng
from quanlydanhba import *
class MainWindow:
    def __init__(self):
        self.main_win = QWidget()
        self.ui = Ui_Quanlydanhba()
        self.ui.setupUi(self.main_win)
        self.lienketnut()


    def lienketnut(self):
#Liên kết các nút
        self.ui.pb_taolienhe.clicked.connect(self.hien_form_them)
        self.ui.pb_luu.clicked.connect(self.luu_lien_he)
        self.ui.pb_huy.clicked.connect(self.an_form)
        self.ui.pb_xoa.clicked.connect(self.xoa_lien_he)
        self.ui.pb_chinhsua.clicked.connect(self.chinh_sua_lien_he)
        self.ui.line_timkiem.textChanged.connect(self.tim_kiem)
        self.ui.groupBox.hide()# Ẩn khung thêm/chỉnh sửa liên hệ khi bấm vào nút thêm liên hệ or chỉnh sửa liên hệ
        # Trạng thái là đang tạo mới hay đang chỉnh sửa
        self.dang_sua = True
#biến trạng thái(flag): đang sửa = false thì có nghĩ là đang thêm liên hệ
# dang sua= true có nghĩ là đang chỉnh sửa liên hệ
        self.hang_dang_sua = None
#dùng để cập nhật chỉnh sửa cho hàng: khi chọn chỉnh sửa liên hệ thì hang_dang_sua= hàng đang chọn

    #Hiển thị khung thêm liên hệ mới
    def hien_form_them(self):
        self.ui.groupBox.show()
        self.ui.lineEdit_ten.text()
        self.ui.lineEdit_sdt.text()
        self.ui.lineEdit_email.text()
        self.dang_sua = False #khi thêm liên hệ thì dang_sua là sai nghĩa là nó đang thêm liên hệ mới
        self.hang_dang_sua = None #hàng dang sửa = 0 vì lúc này đang thêm liên hệ

    # ẩn khung thêm liên hệ bằng nút hủy
    def an_form(self):
        self.ui.groupBox.hide()
        self.ui.lineEdit_ten.clear()#hàm clear dùng để xóa những dữ liệu cũ trong ô
        self.ui.lineEdit_sdt.clear()# để đảm bảo khi bấm hủy thì dữ liệu trông ô sẽ đc xóa hết
        self.ui.lineEdit_email.clear() # để khi bấm thêm hoặc chỉnh sửa liên hệ sẽ hiện các ô trống hoặc dữ liệu hàng đang chọn

    # === Lưu liên hệ ===
    def luu_lien_he(self):
        ten = self.ui.lineEdit_ten.text().strip()
        sdt = self.ui.lineEdit_sdt.text().strip()
        email = self.ui.lineEdit_email.text().strip()

        if not ten or not sdt:
            QMessageBox.warning(self.main_win, "Lỗi", "Vui lòng nhập đầy đủ Tên và Số điện thoại!")
            return

        if self.dang_sua and self.hang_dang_sua is not None:
            # Cập nhật
            self.ui.bangdanhba.setItem(self.hang_dang_sua, 0, QTableWidgetItem(ten))
            self.ui.bangdanhba.setItem(self.hang_dang_sua, 1, QTableWidgetItem(sdt))
            self.ui.bangdanhba.setItem(self.hang_dang_sua, 2, QTableWidgetItem(email))
            QMessageBox.information(self.main_win, "Cập nhật", "Đã chỉnh sửa thông tin liên hệ.")
        else:
            # Thêm mới
            row = self.ui.bangdanhba.rowCount()
            self.ui.bangdanhba.insertRow(row)
            self.ui.bangdanhba.setItem(row, 0, QTableWidgetItem(ten))
            self.ui.bangdanhba.setItem(row, 1, QTableWidgetItem(sdt))
            self.ui.bangdanhba.setItem(row, 2, QTableWidgetItem(email))
            QMessageBox.information(self.main_win, "Thành công", "Đã thêm liên hệ mới.")

        self.an_form()

    # === Xóa liên hệ ===
    def xoa_lien_he(self):
        hang = self.ui.bangdanhba.currentRow()
        if hang < 0:
            QMessageBox.warning(self.main_win, "Thông báo", "Vui lòng chọn liên hệ cần xóa.")
            return

        ten = self.ui.bangdanhba.item(hang, 0).text()
        xacnhan = QMessageBox.question(
            self.main_win, "Xác nhận", f"Bạn có chắc muốn xóa '{ten}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if xacnhan == QMessageBox.StandardButton.Yes:
            self.ui.bangdanhba.removeRow(hang)
            QMessageBox.information(self.main_win, "Đã xóa", "Xóa liên hệ thành công.")

    # === Chỉnh sửa liên hệ ===
    def chinh_sua_lien_he(self):
        hang = self.ui.bangdanhba.currentRow()
        if hang < 0:
            QMessageBox.warning(self.main_win, "Thông báo", "Vui lòng chọn liên hệ cần chỉnh sửa.")
            return

        self.dang_sua = True
        self.hang_dang_sua = hang
        self.ui.groupBox.show()

        # Đổ dữ liệu lên form
        self.ui.lineEdit_ten.setText(self.ui.bangdanhba.item(hang, 0).text())
        self.ui.lineEdit_sdt.setText(self.ui.bangdanhba.item(hang, 1).text())
        self.ui.lineEdit_email.setText(self.ui.bangdanhba.item(hang, 2).text())

    # === Tìm kiếm liên hệ ===
    def tim_kiem(self):
        tu_khoa = self.ui.line_timkiem.text().lower()
        for hang in range(self.ui.bangdanhba.rowCount()):
            ten = self.ui.bangdanhba.item(hang, 0).text().lower() if self.ui.bangdanhba.item(hang, 0) else ""
            hien = tu_khoa in ten
            self.ui.bangdanhba.setRowHidden(hang, not hien)

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
