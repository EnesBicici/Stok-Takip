from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from stokekle_ui import Ui_Form
from PyQt5 import QtCore
from datetime import datetime
from veritabani import Veritabani
from stok import Stok,Urun
from PyQt5.QtCore import pyqtSignal

class StokEkleSayfa(QWidget):
    stokeklesinyal = pyqtSignal()
    def __init__(self) -> None:
        super().__init__()
        self.stokform = Ui_Form()
        self.stokform.setupUi(self)
        self.stokform.ekleButton.clicked.connect(self.stokekle)

    def stokekle(self):
        urunisim = self.stokform.StokIsim.text()
        birim = self.stokform.birimBox.currentIndex()
        miktar = self.stokform.miktarBox.value()
        aciklama = self.stokform.aciklama.toPlainText()
        birimfiyat = self.stokform.fiyatBox.value()

        yanit = QMessageBox.warning(self,"Stok Ekle","Stok eklemek istediğine emin misin?",QMessageBox.Yes,QMessageBox.No)
        if yanit==QMessageBox.No:
            return
        Urun.urunekle(urunisim,aciklama,"urun.jpg")
        Veritabani.query("select id from urun where ad=?",(urunisim,))
        urunid = Veritabani.fetchone()[0]
        Stok.stokekle(urunid,birim,miktar,birimfiyat)
        QMessageBox.information(self,"Stok Ekle","Stok ekleme işlemi tamamlandı",QMessageBox.Ok)
        self.stokeklesinyal.emit()
