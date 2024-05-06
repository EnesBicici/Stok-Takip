from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from hareketler_ui import Ui_Form
from PyQt5 import QtCore
from datetime import datetime
from veritabani import Veritabani

class HareketSayfa(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.hareketform = Ui_Form()
        self.hareketform.setupUi(self)

    def goster(self):
        tablo = self.hareketform.tablo
        tablo.setRowCount(0)
        Veritabani.query("SELECT stokid,kullaniciid,eylem,strftime('%d.%m.%Y %H:%M',tarih) as tarih FROM hareketler")
        hareketler = Veritabani.fetchall()
        self.show()
        if hareketler is None:
            return
        tablo.setRowCount(len(hareketler))
        satir = 0
        tablo.setColumnWidth(0, 100)
        tablo.setColumnWidth(1, 140)
        tablo.setColumnWidth(2, 165)
        tablo.setColumnWidth(3, 100)

        for stokid, kullaniciid, eylem, tarih in hareketler:
            Veritabani.query('SELECT urunid from stok where id=?',(stokid,))
            urunid = Veritabani.fetchone()[0]
            Veritabani.query('SELECT ad from urun where id=?',(urunid,))
            urunad = Veritabani.fetchone()[0]
            Veritabani.query('SELECT ad,soyad from kullanicilar where id=?',(kullaniciid,))
            kullanici = Veritabani.fetchone()
            uyecell = QTableWidgetItem(kullanici[0] + " " + kullanici[1])
            stokcell = QTableWidgetItem(urunad)
            eylemcell = QTableWidgetItem(eylem)
            tarihcell = QTableWidgetItem(tarih)

            #Hepsinin yazısını ortala
            uyecell.setTextAlignment(QtCore.Qt.AlignCenter)
            stokcell.setTextAlignment(QtCore.Qt.AlignCenter)
            tarihcell.setTextAlignment(QtCore.Qt.AlignCenter)
            eylemcell.setTextAlignment(QtCore.Qt.AlignCenter)

            tablo.setItem(satir, 0, uyecell)
            tablo.setItem(satir, 1, stokcell)
            tablo.setItem(satir, 2, eylemcell)
            tablo.setItem(satir, 3, tarihcell)

            satir+=1

        #tablo.resizeColumnsToContents()
