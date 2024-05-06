import sqlite3

class veritabani:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stok'")
        tablo_var_mi = self.cursor.fetchone()

        if not tablo_var_mi:  # Tablo yok
            self.cursor.execute('CREATE TABLE IF NOT EXISTS stok (ID INTEGER PRIMARY KEY AUTOINCREMENT, urunID TEXT, Birim INTEGER, Miktar INTEGER, Fiyat REAL)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS kullanicilar (ID INTEGER PRIMARY KEY AUTOINCREMENT, kullaniciadi TEXT, sifre TEXT, ad TEXT, soyad TEXT, telefon TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS siparisler (ID INTEGER PRIMARY KEY AUTOINCREMENT,StokID INTEGER,UrunID INTEGER, Miktar INTEGER, ToplamFiyat REAL, Tarih TIMESTAMP)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS urun (ID INTEGER PRIMARY KEY AUTOINCREMENT, Ad TEXT,Aciklama TEXT, Fotograf TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS hareketler (ID INTEGER PRIMARY KEY AUTOINCREMENT, StokID INTEGER,KullaniciID INTEGER,Eylem TEXT, Tarih TIMESTAMP)')


            self.cursor.execute('''INSERT INTO urun (Ad, Aciklama, Fotograf) VALUES 
                ('Apple MacBook Air', 'Hızlı işlemci ve yüksek çözünürlüklü ekranla güçlü bir laptop.', 'laptop.jpg'),
                ('Logitech G Pro Mouse', 'Kablosuz ve ergonomik fare.', 'mouse.jpg'),
                ('Logitech G915 Klavye', 'Işıklandırmalı ve dayanıklı klavye.', 'klavye.png'),
                ('Dell 23 inch Monitör', 'Geniş ekran ve yüksek çözünürlüklü monitör.', 'monitor.jpg'),
                ('Apple Airpods Pro', 'Yüksek kaliteli ses sağlayan kulaklık.', 'kulaklik.jpg'),
                ('Logitech 4K Webcam', 'Yüksek çözünürlüklü ve sesli webcam.', 'webcam.jpg'),
                ('Seagate 2TB Harddisk', 'Yüksek depolama kapasitesine sahip harici harddisk.', 'harddisk.jpg'),
                ('Canon Pixma Yazıcı', 'Renkli ve yüksek çözünürlüklü yazıcı.', 'yazici.jpg'),
                ('Apple Ipad', 'Taşınabilir ve dokunmatik tablet.', 'tablet.jpg'),
                ('TP-LINK Router', 'Hızlı internet bağlantısı sağlayan router.', 'router.jpg');
                ''')
            
            self.cursor.execute('''INSERT INTO stok (urunID, Birim, Miktar, Fiyat) VALUES 
                (1, 0, 10, 40000),
                (2, 0, 20, 2000),
                (3, 0, 15, 2500),
                (4, 0, 5, 12000),
                (5, 0, 12, 5000),
                (6, 0, 8, 2000),
                (7, 0, 25, 1000),
                (8, 0, 6, 1500),
                (9, 0, 18, 25000),
                (10, 0, 10, 900);
                ''')
            
            self.cursor.execute("INSERT INTO kullanicilar (kullaniciadi, sifre, ad, soyad, telefon) VALUES ('enes', '123', 'Enes', 'Biçici', '5323184256')")
            self.connection.commit()

    def query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()
        return self.cursor
    
    def fetchall(self):
        return self.cursor.fetchall()
    
    def fetchone(self):
        return self.cursor.fetchone()
    
Veritabani = veritabani('sql.db')
