# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import os

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(756, 563)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_plain = QtWidgets.QLabel(self.centralwidget)
        self.label_plain.setGeometry(QtCore.QRect(10, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_plain.setFont(font)
        self.label_plain.setObjectName("label_plain")

        self.txt_plain_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(QtCore.QRect(110, 90, 611, 121))
        self.txt_plain_text.setObjectName("txt_plain_text")

        self.label_key = QtWidgets.QLabel(self.centralwidget)
        self.label_key.setGeometry(QtCore.QRect(10, 230, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_key.setFont(font)
        self.label_key.setObjectName("label_key")

        self.txt_key = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_key.setGeometry(QtCore.QRect(110, 230, 151, 31))
        self.txt_key.setObjectName("txt_key")

        self.label_cipher = QtWidgets.QLabel(self.centralwidget)
        self.label_cipher.setGeometry(QtCore.QRect(10, 290, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_cipher.setFont(font)
        self.label_cipher.setObjectName("label_cipher")

        self.txt_cipher_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_cipher_text.setGeometry(QtCore.QRect(110, 290, 611, 121))
        self.txt_cipher_text.setObjectName("txt_cipher_text")

        self.btn_encrypt = QtWidgets.QToolButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(230, 450, 101, 31))
        self.btn_encrypt.setObjectName("btn_encrypt")

        self.btn_decrypt = QtWidgets.QToolButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(490, 450, 101, 31))
        self.btn_decrypt.setObjectName("btn_decrypt")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 756, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "Transposition Cipher"))
        self.label.setText(_translate("MainWindow", "TRANSPOSITION CIPHER"))
        self.label_plain.setText(_translate("MainWindow", "Plain Text:"))
        self.label_key.setText(_translate("MainWindow", "Key:"))
        self.label_cipher.setText(_translate("MainWindow", "Cipher Text:"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())