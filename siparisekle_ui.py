# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'siparisekle.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(724, 587)
        self.oncekiButon = QtWidgets.QPushButton(Form)
        self.oncekiButon.setGeometry(QtCore.QRect(441, 260, 51, 41))
        self.oncekiButon.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/sol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.oncekiButon.setIcon(icon)
        self.oncekiButon.setIconSize(QtCore.QSize(32, 32))
        self.oncekiButon.setObjectName("oncekiButon")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 325, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.stokKod = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.stokKod.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.stokKod.setFont(font)
        self.stokKod.setReadOnly(True)
        self.stokKod.setObjectName("stokKod")
        self.horizontalLayout_5.addWidget(self.stokKod)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
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
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.stokIsim = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.stokIsim.setFont(font)
        self.stokIsim.setObjectName("stokIsim")
        self.horizontalLayout_6.addWidget(self.stokIsim)
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
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.birimIsim = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.birimIsim.setFont(font)
        self.birimIsim.setObjectName("birimIsim")
        self.horizontalLayout_7.addWidget(self.birimIsim)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
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
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.birimFiyat = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.birimFiyat.setFont(font)
        self.birimFiyat.setObjectName("birimFiyat")
        self.horizontalLayout_8.addWidget(self.birimFiyat)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_9.addWidget(self.label_15)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.toplamFiyat = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.toplamFiyat.setFont(font)
        self.toplamFiyat.setObjectName("toplamFiyat")
        self.horizontalLayout_9.addWidget(self.toplamFiyat)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.aciklamaLabel = QtWidgets.QLabel(Form)
        self.aciklamaLabel.setGeometry(QtCore.QRect(120, 340, 451, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.aciklamaLabel.setFont(font)
        self.aciklamaLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aciklamaLabel.setScaledContents(False)
        self.aciklamaLabel.setWordWrap(True)
        self.aciklamaLabel.setObjectName("aciklamaLabel")
        self.kaydetButon = QtWidgets.QPushButton(Form)
        self.kaydetButon.setGeometry(QtCore.QRect(270, 470, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kaydetButon.setFont(font)
        self.kaydetButon.setObjectName("kaydetButon")
        self.sonrakiButon = QtWidgets.QPushButton(Form)
        self.sonrakiButon.setGeometry(QtCore.QRect(551, 260, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.sonrakiButon.setFont(font)
        self.sonrakiButon.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/sağ.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sonrakiButon.setIcon(icon1)
        self.sonrakiButon.setIconSize(QtCore.QSize(32, 32))
        self.sonrakiButon.setObjectName("sonrakiButon")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(30, 340, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.fotograf = QtWidgets.QLabel(Form)
        self.fotograf.setGeometry(QtCore.QRect(370, 40, 301, 200))
        self.fotograf.setText("")
        self.fotograf.setScaledContents(True)
        self.fotograf.setObjectName("fotograf")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sipariş Ekle"))
        self.label_5.setText(_translate("Form", "Stok Kodu"))
        self.stokKod.setText(_translate("Form", "0001"))
        self.label_6.setText(_translate("Form", "Ürün İsmi"))
        self.stokIsim.setText(_translate("Form", "Apple MacBook Air"))
        self.label_8.setText(_translate("Form", "Birimi"))
        self.birimIsim.setText(_translate("Form", "Adet"))
        self.label_9.setText(_translate("Form", "Miktarı"))
        self.label_10.setText(_translate("Form", "Birim Fiyat"))
        self.birimFiyat.setText(_translate("Form", "TextLabel"))
        self.label_15.setText(_translate("Form", "Toplam Fiyat"))
        self.toplamFiyat.setText(_translate("Form", "TextLabel"))
        self.aciklamaLabel.setText(_translate("Form", "abc"))
        self.kaydetButon.setText(_translate("Form", "Sipariş Ekle"))
        self.label_11.setText(_translate("Form", "Açıklama"))
