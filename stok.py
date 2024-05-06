from veritabani import Veritabani
from datetime import datetime

class Stok:
    def __init__(self,ID, urunID, Birim, Miktar, Fiyat):
        self.id = ID
        self.urunid = urunID
        self.birim = Birim
        self.miktar = Miktar
        self.fiyat = Fiyat

    def stokguncelle(self,KullaniciID, Birim=None, Miktar=None):
        if Birim is None and Miktar is not None:
            Veritabani.query('update stok set miktar=? where id=?',(Miktar,self.id))
            self.hareketekle(self.id, KullaniciID, "Miktar Güncelleme")
        elif Birim is not None and Miktar is None:
            Veritabani.query('update stok set birim=? where id=?',(Birim,self.id))
            self.hareketekle(self.id, KullaniciID, "Birim Güncelleme")
        else:
            Veritabani.query('update stok set birim=?,miktar=? where id=?',(Birim,Miktar,self.id))
            self.hareketekle(self.id, KullaniciID, "Miktar ve Birim Güncelleme")

    @staticmethod
    def hareketekle(stokid, kullaniciid, eylem):
        Veritabani.query('insert into hareketler(stokid,kullaniciid,eylem,tarih) values(?,?,?,?)',(stokid, kullaniciid, eylem, datetime.now()))

    def fiyatguncelle(self,fiyat,KullaniciID):
        Veritabani.query('update stok set fiyat=? where id=?',(fiyat,self.id))
        self.hareketekle(self.id, KullaniciID, "Fiyat Güncelleme")

    @staticmethod
    def stokekle(urunid,birim,miktar,fiyat):
        Veritabani.query('insert into stok(urunid,birim,miktar,fiyat) values(?,?,?,?)', (urunid,birim,miktar,fiyat))

    def sil(self):
        Veritabani.query('delete from stok where id=?',(self.id,))

class Urun:
    def __init__(self,urunid, ad, aciklama, fotograf):
        self.id = urunid
        self.ad = ad
        self.aciklama = aciklama
        self.fotograf = fotograf

    @staticmethod
    def urunekle(ad,aciklama,fotograf):
        Veritabani.query('insert into urun(ad,aciklama,fotograf) values(?,?,?)', (ad,aciklama,fotograf))

    def isimguncelle(self, isim):
        Veritabani.query('update urun set ad=? where id=?',(isim,self.id))

class Siparis:
    def __init__(self,id,stokid,urunid,miktar,toplamfiyat,tarih):
        self.id = id
        self.stokid = stokid
        self.urunid = urunid
        self.miktar = miktar
        self.toplamfiyat = toplamfiyat
        self.tarih = tarih

    @staticmethod
    def siparisekle(stokid,urunid,miktar,toplamfiyat,kullaniciid):
        tarih = datetime.now()
        Veritabani.query('insert into siparisler(stokid,urunid,miktar,toplamfiyat,tarih) values(?,?,?,?,?)', (stokid,urunid,miktar,toplamfiyat,tarih))
        Veritabani.query('select miktar from stok where id=?',(stokid,))
        suankimiktar = Veritabani.fetchone()[0]
        Veritabani.query('update stok set miktar=? where id=?',(suankimiktar-miktar, stokid))
        Stok.hareketekle(stokid, kullaniciid, "Siparis Ekleme")

    def siparisiptal(self,kullaniciid):
        Veritabani.query('delete from siparisler where id=?',(self.id,))
        Veritabani.query('select miktar from stok where id=?',(self.stokid,))
        suankimiktar = Veritabani.fetchone()[0]
        Veritabani.query('update stok set miktar=? where id=?',(suankimiktar+self.miktar, self.stokid))
        Stok.hareketekle(self.stokid, kullaniciid, "Siparis İptali")

class Kullanici:
    def __init__(self,id,kullaniciadi, sifre, ad, soyad, telefon):
        self.id = id
        self.kullaniciadi = kullaniciadi
        self.sifre = sifre
        self.ad = ad
        self.soyad = soyad
        self.telefon = telefon

    @staticmethod
    def kayitol(kullaniciadi, sifre, ad, soyad, telefon):
        Veritabani.query('INSERT INTO kullanicilar (kullaniciadi, sifre, ad, soyad, telefon) VALUES(?, ?, ?, ?, ?)', (kullaniciadi, sifre, ad, soyad, telefon))
    
