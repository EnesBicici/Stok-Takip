from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from siparisiptal_ui import Ui_Form
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from veritabani import Veritabani
from datetime import datetime
from stok import Stok,Urun,Siparis


class SiparisIptalSayfa(QWidget):
    siparis_iptal_sinyal = pyqtSignal()
    def __init__(self) -> None:
        super().__init__()
        self.siparislisteform = Ui_Form()
        self.siparislisteform.setupUi(self)
        self.siparislisteform.iptalButon.clicked.connect(self.siparisiptal)

    def goster(self, uye):
        self.uye = uye
        tablo = self.siparislisteform.tablo
        Veritabani.query("SELECT id,stokid,urunid,miktar,toplamfiyat,strftime('%d.%m.%Y %H:%M',tarih) as tarih from siparisler")
        siparisler = Veritabani.fetchall()
        tablo.setRowCount(0)
        self.show()
        if siparisler is None:
            return
        siparisliste = []
        for siparis in siparisler:
            siparisliste.append(Siparis(*siparis))
        self.siparisler = siparisliste
        
        tablo.setRowCount(len(siparisler))
        satir = 0
        tablo.setColumnWidth(0, 60)
        tablo.setColumnWidth(1, 60)
        tablo.setColumnWidth(2, 160)
        tablo.setColumnWidth(3, 100)
        tablo.setColumnWidth(4, 140)
        tablo.setColumnWidth(5, 140)

        for id,stokid,urunid,miktar,toplamfiyat,tarih in siparisler:
            Veritabani.query('SELECT Ad from urun WHERE ID = ?', (urunid,))
            urunad = Veritabani.fetchone()[0]
            sipariskodcell = QTableWidgetItem(str(id))
            stokkodcell = QTableWidgetItem(str(stokid))
            uruncell = QTableWidgetItem(urunad)
            miktarcell = QTableWidgetItem(str(miktar))
            tarihcell = QTableWidgetItem(tarih)
            fiyatcell= QTableWidgetItem(f"{toplamfiyat} TL")


            #Hepsinin yazısını ortala
            sipariskodcell.setTextAlignment(QtCore.Qt.AlignCenter)
            stokkodcell.setTextAlignment(QtCore.Qt.AlignCenter)
            uruncell.setTextAlignment(QtCore.Qt.AlignCenter)
            miktarcell.setTextAlignment(QtCore.Qt.AlignCenter)
            tarihcell.setTextAlignment(QtCore.Qt.AlignCenter)
            fiyatcell.setTextAlignment(QtCore.Qt.AlignCenter)



            tablo.setItem(satir, 0, sipariskodcell)
            tablo.setItem(satir, 1, stokkodcell)
            tablo.setItem(satir, 2, uruncell)
            tablo.setItem(satir, 3, miktarcell)
            tablo.setItem(satir, 4, tarihcell)
            tablo.setItem(satir, 5, fiyatcell)
            satir+=1

        #tablo.resizeColumnsToContents()

    def siparisiptal(self):
        if self.siparislisteform.tablo.rowCount() < 1: 
            return
        seciliindex = self.siparislisteform.tablo.currentRow()
        if seciliindex < 0:
            return
        yanit = QMessageBox.warning(self, "Sipariş İptal","Sipariş iptal işlemini onaylıyor musunuz?", QMessageBox.Yes, QMessageBox.No)
        
        if yanit == QMessageBox.No:
            return
        self.siparislisteform.tablo.removeRow(seciliindex)
        siparis = self.siparisler[seciliindex]
        siparis.siparisiptal(self.uye.id)
        self.siparis_iptal_sinyal.emit()
        QMessageBox.information(self, "Sipariş İptal","Siparişiniz iptal edildi.", QMessageBox.Ok)
        