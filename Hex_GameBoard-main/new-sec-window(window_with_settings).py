# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new-sec-window.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(754, 588)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255),stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255))\n"
"")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 10, 721, 561))
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 2px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 70, 721, 51))
        font = QtGui.QFont()
        font.setFamily("Orpheus")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: none;\n"
"border: none;\n"
"color: black;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(0, 510, 721, 51))
        font = QtGui.QFont()
        font.setFamily("Orpheus")
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"color: black;\n"
"background-color: rgba(255,255,255, 30);\n"
"border: 2px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width:230px;\n"
"height: 50px\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/reply_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 170, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Orpheus")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: none;\n"
"border: none;\n"
"color: black;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 230, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Orpheus")
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: none;\n"
"border: none;\n"
"color: black;")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 170, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Orpheus")
        font.setPointSize(22)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border-radius: 7px;\n"
"width:230px;\n"
"height: 50px;\n"
"background-color: none;\n"
"border: none;\n"
"color: black;\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/check_circle_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 170, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Orpheus")
        font.setPointSize(22)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"border-radius: 7px;\n"
"width:230px;\n"
"height: 50px;\n"
"background-color: none;\n"
"border: none;\n"
"color: black;\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons/cancel_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(490, 230, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Orpheus")
        font.setPointSize(22)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Настройки"))
        self.pushButton.setText(_translate("Dialog", "Выйти"))
        self.label_2.setText(_translate("Dialog", "Музыка"))
        self.label_3.setText(_translate("Dialog", "Разрешение"))
        self.pushButton_2.setText(_translate("Dialog", "Вкл."))
        self.pushButton_3.setText(_translate("Dialog", "Выкл."))
        self.comboBox.setItemText(0, _translate("Dialog", "1920x1080"))
        self.comboBox.setItemText(1, _translate("Dialog", "1366x768"))
        self.comboBox.setItemText(2, _translate("Dialog", "1280x720"))
        self.comboBox.setItemText(3, _translate("Dialog", "800x600"))
import res_new_rc
import res_sec_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
