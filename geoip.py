#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
import pygeoip, sys, socket


def msg_box(title, message):
    w = QTGui.QWidget()
    QTGui.QMessageBox.information(w, title, message)

def update_search_list(self, data):
    self.search_list.addItem(data)


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PyGeoIP_Window(object):
    def setupUi(self, PyGeoIP_Window):
        PyGeoIP_Window.setObjectName(_fromUtf8("PyGeoIP_Window"))
        PyGeoIP_Window.resize(460, 570)
        PyGeoIP_Window.setStyleSheet(_fromUtf8("background-color: rgb(170, 0, 0);"))
        self.centralwidget = QtGui.QWidget(PyGeoIP_Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 20, 441, 51))
        self.frame.setStyleSheet(_fromUtf8("background-color: rgb(140, 0, 0);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.ip_textbox = QtGui.QLineEdit(self.frame)
        self.ip_textbox.setGeometry(QtCore.QRect(110, 10, 221, 31))
        self.ip_textbox.setStyleSheet(_fromUtf8("background-color: rgb(171, 171, 171);\n"
""))
        self.ip_textbox.setObjectName(_fromUtf8("ip_textbox"))
        self.ip_label = QtGui.QLabel(self.frame)
        self.ip_label.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.ip_label.setObjectName(_fromUtf8("ip_label"))
        self.search_btn = QtGui.QPushButton(self.frame)
        self.search_btn.setGeometry(QtCore.QRect(350, 10, 81, 31))
        self.search_btn.setMinimumSize(QtCore.QSize(0, 31))
        self.search_btn.setStyleSheet(_fromUtf8("font: 78 14pt \"Sans Serif\";color:#55ffff;\n"
"background-color: rgb(170, 0, 0);\n"
""))
        self.search_btn.setObjectName(_fromUtf8("search_btn"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 150, 441, 381))
        self.frame_2.setStyleSheet(_fromUtf8("background-color: rgb(140, 0, 0);"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.search_list = QtGui.QListWidget(self.frame_2)
        self.search_list.setGeometry(QtCore.QRect(10, 10, 421, 361))
        self.search_list.setStyleSheet(_fromUtf8("background-color: rgb(171, 171, 171);\n"
""))
        self.search_list.setObjectName(_fromUtf8("search_list"))
        self.search_btn.clicked.connect(self.search)
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 90, 441, 51))
        self.frame_3.setStyleSheet(_fromUtf8("background-color: rgb(140, 0, 0);"))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.info_bar = QtGui.QLabel(self.frame_3)
        self.info_bar.setGeometry(QtCore.QRect(10, 10, 411, 31))
        self.info_bar.setObjectName(_fromUtf8("info_bar"))
        PyGeoIP_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PyGeoIP_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        PyGeoIP_Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PyGeoIP_Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PyGeoIP_Window.setStatusBar(self.statusbar)

        self.retranslateUi(PyGeoIP_Window)
        QtCore.QMetaObject.connectSlotsByName(PyGeoIP_Window)

    def retranslateUi(self, PyGeoIP_Window):
        PyGeoIP_Window.setWindowTitle(_translate("PyGeoIP_Window", "~::: GeoIP-URL by Aink :::~", None))
        self.ip_label.setText(_translate("PyGeoIP_Window", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;  color:#55ffff;\">IP / URL :</span></p></body></html>", None))
        self.search_btn.setWhatsThis(_translate("PyGeoIP_Window", "<html><head/><body><p>KLik Tombol CARI untuk Pencarian</p></body></html>", None))
        self.search_btn.setText(_translate("PyGeoIP_Window", "CARI", None))
        self.info_bar.setText(_translate("PyGeoIP_Window", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;  color:#55ffff;\">Tips: Masukan Alamat IP Ke Kolom Dan Klik Pencarian</span></p></body></html>", None))

    def search(self):
            message = ''
            result_count = 0
            gip = pygeoip.GeoIP('GeoLiteCity.dat')
            ip = self.ip_textbox.text()
            try:
                ip = socket.gethostbyname(str(ip))
                message = "Host: %s Is Currently Available" % (str(ip))
            except socket.error, e:
                message = "Host: %s Is Currently Unavailable" % (str(ip))
            self.info_bar.setText(message)
            self.search_list.clear()
            try:
                rec = gip.record_by_addr(str(ip))
                for key, val in rec.items():
                    update_search_list(self, "[*] %s => %s" % (key,val))
                    result_count += 1
                msg_box("Search Complete", "%d Results Were Found For %s"
                % (result_count, str(ip)))
            except Exception, e:
                msg_box("", str(e))
                msg_box("Search Complete", "No Results Were Found For %s" % (str(ip)))
                return

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PyGeoIP_Window = QtGui.QMainWindow()
    ui = Ui_PyGeoIP_Window()
    ui.setupUi(PyGeoIP_Window)
    PyGeoIP_Window.show()
    sys.exit(app.exec_())

