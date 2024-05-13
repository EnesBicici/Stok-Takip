from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PyQt5 import QtGui
from giris_ui import Ui_MainWindow
from stok import Kullanici
from ana import AnaSayfa
from kayit import KayitSayfa
from veritabani import Veritabani
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtCore import Qt

class arayuz(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.qtprogram = Ui_MainWindow()
        self.qtprogram.setupUi(self)
        self.qtprogram.girisButon.clicked.connect(self.girisyap)
        self.anasayfa = AnaSayfa()
        kayitsayfa = KayitSayfa()
        self.qtprogram.kayitButon.clicked.connect(lambda: kayitsayfa.show())
        kayitsayfa.kayit_sinyal.connect(self.kayitol)
        shortcut = QShortcut(QKeySequence("Return"), self)
        shortcut.activated.connect(self.girisyap)
        self.qtprogram.girisButon.setFocusPolicy(Qt.StrongFocus)
        self.qtprogram.sifreLine.setEchoMode(QLineEdit.Password)

    def girisyap(self):
        kullaniciadi = self.qtprogram.adLine.text()
        sifre = self.qtprogram.sifreLine.text()
        Veritabani.query('SELECT * FROM kullanicilar WHERE kullaniciadi = ? AND sifre = ?', (kullaniciadi, sifre))
        uye = Veritabani.fetchone()

        if uye is None:
            QMessageBox.warning(self, "Giris", "Kullanıcı adı veya şifre yanlış.", QMessageBox.Ok)
            return
        uye = Kullanici(uye[0],uye[1],uye[2],uye[3],uye[4],uye[5])
        self.anasayfa.goster(uye)
        self.close()

    def kayitol(self,liste):
        Kullanici.kayitol(liste[0],liste[1],liste[2],liste[3],liste[4])


app = QApplication([])
pencere = arayuz()
pencere.show()
app.exec_()
