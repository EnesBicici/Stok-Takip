# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ekle.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(324, 423)
        self.ekleButton = QtWidgets.QPushButton(Form)
        self.ekleButton.setGeometry(QtCore.QRect(100, 350, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ekleButton.setFont(font)
        self.ekleButton.setObjectName("ekleButton")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 260, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 285, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.StokIsim = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.StokIsim.setFont(font)
        self.StokIsim.setObjectName("StokIsim")
        self.horizontalLayout_6.addWidget(self.StokIsim)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.birimBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.birimBox.setFont(font)
        self.birimBox.setObjectName("birimBox")
        self.birimBox.addItem("")
        self.birimBox.addItem("")
        self.birimBox.addItem("")
        self.birimBox.addItem("")
        self.horizontalLayout_7.addWidget(self.birimBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.miktarBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.miktarBox.setFont(font)
        self.miktarBox.setMaximum(9999)
        self.miktarBox.setProperty("value", 1000)
        self.miktarBox.setObjectName("miktarBox")
        self.horizontalLayout_7.addWidget(self.miktarBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.fiyatBox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.fiyatBox.setFont(font)
        self.fiyatBox.setMinimum(0.01)
        self.fiyatBox.setMaximum(1000000.0)
        self.fiyatBox.setObjectName("fiyatBox")
        self.horizontalLayout_8.addWidget(self.fiyatBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.aciklama = QtWidgets.QTextEdit(Form)
        self.aciklama.setGeometry(QtCore.QRect(130, 260, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.aciklama.setFont(font)
        self.aciklama.setObjectName("aciklama")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Stok Ekle"))
        self.ekleButton.setText(_translate("Form", "Ekle"))
        self.label_5.setText(_translate("Form", "Açıklama"))
        self.label_6.setText(_translate("Form", "Ürün İsmi"))
        self.label_8.setText(_translate("Form", "Birimi"))
        self.birimBox.setItemText(0, _translate("Form", "Adet"))
        self.birimBox.setItemText(1, _translate("Form", "Gram"))
        self.birimBox.setItemText(2, _translate("Form", "Kilogram"))
        self.birimBox.setItemText(3, _translate("Form", "Ton"))
        self.label_9.setText(_translate("Form", "Miktarı"))
        self.label_10.setText(_translate("Form", "Fiyat"))
        self.aciklama.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
