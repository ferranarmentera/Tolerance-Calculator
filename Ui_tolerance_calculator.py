# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\tec03\Documents\GitHub\Python_vstudio\tolerance_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(492, 279)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(90, 60, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 30, 161, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(260, 170, 181, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 60, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(270, 30, 161, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(300, 140, 111, 16))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(300, 200, 111, 16))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 110, 181, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(90, 140, 151, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Tolerance Calculator"))
        self.label.setText(_translate("Form", "Enter dimension value "))
        self.label_2.setText(_translate("Form", "Chose process quality level"))
        self.label_3.setText(_translate("Form", "Tolerance field feasible"))
        self.comboBox.setItemText(0, _translate("Form", "1 Cavity"))
        self.comboBox.setItemText(1, _translate("Form", "2  Cavities"))
        self.comboBox.setItemText(2, _translate("Form", "4  Cavities"))
        self.comboBox.setItemText(3, _translate("Form", "6  Cavities"))
        self.comboBox.setItemText(4, _translate("Form", "8  Cavities"))
        self.comboBox.setItemText(5, _translate("Form", "16 Cavities"))
        self.comboBox.setItemText(6, _translate("Form", "32 Cavities"))
        self.comboBox.setItemText(7, _translate("Form", "64 Cavities"))
        self.comboBox_2.setItemText(0, _translate("Form", "Coarse"))
        self.comboBox_2.setItemText(1, _translate("Form", "Medium"))
        self.comboBox_2.setItemText(2, _translate("Form", "High"))
        self.label_4.setText(_translate("Form", "Chose the material "))
        self.comboBox_3.setItemText(0, _translate("Form", "POM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
