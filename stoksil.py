from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from stoksil_ui import Ui_Form
from PyQt5 import QtCore
from datetime import datetime
from veritabani import Veritabani
from stok import Stok,Urun
from PyQt5.QtCore import pyqtSignal

class StokSilSayfa(QWidget):
    stoksilsinyal = pyqtSignal(int)
    def __init__(self) -> None:
        super().__init__()
        self.stokform = Ui_Form()
        self.stokform.setupUi(self)
        self.stokform.silButon.clicked.connect(self.stoksil)

    def goster(self):
        Veritabani.query("SELECT * FROM stok")
        sql = Veritabani.fetchall()
        self.stokform.stokBox.clear()
        self.show()
        if sql is None:
            return
        stok = []
        for kayit in sql:
            stok.append(Stok(*kayit))
        self.stoklar = stok
        for stok in self.stoklar:
            Veritabani.query('select ad from urun where id=?',(stok.urunid,))
            urunad = Veritabani.fetchone()[0]
            self.stokform.stokBox.addItem(urunad, stok.id)

    def stoksil(self):
        yanit = QMessageBox.warning(self,"Stok Sil","Seçili stoğu silmek istediğine emin misin?",QMessageBox.Yes,QMessageBox.No)
        if yanit==QMessageBox.No:
            return
        stokindex = self.stokform.stokBox.currentIndex()
        stok = self.stoklar[stokindex]
        stok.sil()
        self.stoksilsinyal.emit(stokindex)
        QMessageBox.information(self,"Stok Sil","Stok silme işlemi tamamlandı.",QMessageBox.Ok)
        self.stokform.stokBox.removeItem(stokindex)

