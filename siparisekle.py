from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from siparisekle_ui import Ui_Form
from PyQt5 import QtCore
from datetime import datetime
from veritabani import Veritabani
from stok import Stok,Urun,Siparis
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtGui

class SiparisEkleSayfa(QWidget):
    sipariseklesinyal = pyqtSignal()
    def __init__(self) -> None:
        super().__init__()
        self.form = Ui_Form()
        self.form.setupUi(self)
        self.index = 0
        self.form.miktarBox.valueChanged.connect(self.toplamfiyatguncelle)
        self.form.kaydetButon.clicked.connect(self.siparisekle)
        self.form.oncekiButon.clicked.connect(self.onceki)
        self.form.sonrakiButon.clicked.connect(self.sonraki)

    def goster(self, uye):
        self.uye = uye
        self.show()
        self.index = 0
        Veritabani.query("SELECT * FROM stok")
        sql = Veritabani.fetchall()
        stok = []
        for kayit in sql:
            stok.append(Stok(*kayit))
        self.stoklar = stok
        self.stokguncelle()

    def sonraki(self):
        self.index += 1
        if len(self.stoklar) == self.index:
            self.index = 0
        self.stokguncelle()

    def onceki(self):
        self.index -= 1
        if self.index == -1:
            self.index = len(self.stoklar)-1
        self.stokguncelle()

    def stokgoster(self, yeni_indeks):
        self.index = yeni_indeks
        self.stokguncelle()

    def stokguncelle(self):
        stok = self.stoklar[self.index]
        Veritabani.query('select * from urun where id=?',(stok.urunid,))
        urunsql = Veritabani.fetchone()
        urun = Urun(*urunsql)
        self.form.fotograf.setPixmap(QtGui.QPixmap("fotograflar/" + urun.fotograf))
        self.form.stokKod.setText(str(stok.id))
        self.form.stokIsim.setText(urun.ad)
        birim = "Adet"
        if stok.birim == 1:
            birim = "Gram"
        elif stok.birim == 2:
            birim = "Kilogram"
        elif stok.birim == 3:
            birim = "Ton"
        self.form.miktarBox.setMaximum(stok.miktar)
        self.form.miktarBox.setValue(1)
        self.form.aciklamaLabel.setText(urun.aciklama)
        toplamfiyat = stok.fiyat*self.form.miktarBox.value()
        self.form.birimFiyat.setText(f"{stok.fiyat} TL")
        self.form.toplamFiyat.setText(f"{toplamfiyat} TL")
        self.form.birimIsim.setText(birim)
    
    def toplamfiyatguncelle(self):
        stok = self.stoklar[self.index]
        toplamfiyat = stok.fiyat*self.form.miktarBox.value()
        self.form.toplamFiyat.setText(f"{toplamfiyat} TL")

    def siparisekle(self):
        yanit = QMessageBox.warning(self,"Sipariş Ekle","Sipariş eklemek istediğine emin misin?",QMessageBox.Yes,QMessageBox.No)
        if yanit==QMessageBox.No:
            return
        miktar = self.form.miktarBox.value()
        stok = self.stoklar[self.index]
        toplamfiyat = stok.fiyat*self.form.miktarBox.value()
        Siparis.siparisekle(stok.id, stok.urunid, miktar, toplamfiyat,self.uye.id)
        self.sipariseklesinyal.emit()
        self.form.miktarBox.setMaximum(stok.miktar-miktar)
        self.form.miktarBox.setValue(1)
        QMessageBox.information(self,"Sipariş Ekle","Sipariş ekleme işlemi tamamlandı",QMessageBox.Ok)
