from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
from ana_ui import Ui_MainWindow
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtGui
from veritabani import Veritabani
from stok import *
from hareketler import HareketSayfa
from stokekle import StokEkleSayfa
from stoksil import StokSilSayfa
from siparisekle import SiparisEkleSayfa
from siparisiptal import SiparisIptalSayfa

class AnaSayfa(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.anasayfa = Ui_MainWindow()
        self.anasayfa.setupUi(self)
        self.index = 0
        self.anasayfa.sonrakiButon.clicked.connect(self.sonraki)
        self.anasayfa.oncekiButon.clicked.connect(self.onceki)
        self.anasayfa.kaydetButon.clicked.connect(self.kaydet)
        self.listeguncelle()
        self.stokguncelle()
        hareketsayfa = HareketSayfa()
        self.anasayfa.stokhareketleri.triggered.connect(lambda: hareketsayfa.goster())
        stokeklesayfa = StokEkleSayfa()
        self.anasayfa.stokekleme.triggered.connect(lambda: stokeklesayfa.show())
        stokeklesayfa.stokeklesinyal.connect(self.listeguncelle)
        stoksilsayfa = StokSilSayfa()
        stoksilsayfa.stoksilsinyal.connect(self.stoksil)
        self.anasayfa.stoksil.triggered.connect(lambda: stoksilsayfa.goster())
        sipariseklesayfa = SiparisEkleSayfa()
        self.anasayfa.siparisEkle.triggered.connect(lambda: sipariseklesayfa.goster(self.uye))
        sipariseklesayfa.sipariseklesinyal.connect(self.guncelle)
        siparisiptalsayfa = SiparisIptalSayfa()
        self.anasayfa.siparisIptal.triggered.connect(lambda: siparisiptalsayfa.goster(self.uye))
        siparisiptalsayfa.siparis_iptal_sinyal.connect(self.guncelle)


    def goster(self, uye):
        self.uye = uye
        self.show()
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
        self.anasayfa.fotograf.setPixmap(QtGui.QPixmap("fotograflar/" + urun.fotograf))
        self.anasayfa.stokKod.setText(str(stok.id))
        self.anasayfa.StokIsim.setText(urun.ad)
        self.anasayfa.birimBox.setCurrentIndex(stok.birim)
        self.anasayfa.miktarBox.setValue(stok.miktar)
        self.anasayfa.aciklamaLabel.setText(urun.aciklama)
        self.anasayfa.fiyatBox.setValue(stok.fiyat)

    def kaydet(self):
        yanit = QMessageBox.warning(self,"Stok","Kaydetmek istediğinize emin misiniz?",QMessageBox.Yes,QMessageBox.No)
        if yanit == QMessageBox.No :
            return
        stok = self.stoklar[self.index]
        Veritabani.query('select * from urun where id=?',(stok.urunid,))
        urunsql = Veritabani.fetchone()
        urun = Urun(*urunsql)
        stokisim = self.anasayfa.StokIsim.text()
        birim = self.anasayfa.birimBox.currentIndex()
        miktar = self.anasayfa.miktarBox.value()
        fiyat = self.anasayfa.fiyatBox.value()
        if fiyat != stok.fiyat:
            stok.fiyatguncelle(fiyat,self.uye.id)
        if urun.ad !=stokisim:
            urun.isimguncelle(stokisim)
        if birim != stok.birim and miktar!=stok.miktar:
            stok.stokguncelle(self.uye.id, birim, miktar)
        elif birim != stok.birim and miktar==stok.miktar:
            stok.stokguncelle(self.uye.id, birim)
        elif birim == stok.birim and miktar!=stok.miktar:
            stok.stokguncelle(self.uye.id, None, miktar)
        self.listeguncelle()
        QMessageBox.information(self,"Stok","Kaydedildi",QMessageBox.Ok)

    def listeguncelle(self):
        Veritabani.query("SELECT * FROM stok")
        sql = Veritabani.fetchall()
        stok = []
        for kayit in sql:
            stok.append(Stok(*kayit))
        self.stoklar = stok

    def stoksil(self, index):
        if self.index == index:
            self.index = index-1
        self.guncelle()

    def guncelle(self):
        self.listeguncelle()
        self.stokguncelle()
