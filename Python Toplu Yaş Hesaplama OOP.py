class dogumyili:
    def __init__(self,dogum,yil=2024):
        self.dogum= dogum
        self.yil = yil

    def hesaplama(self):
        return self.yil-self.dogum

    def yazdirma(self):
        print("yaşınız:", self.hesaplama())


metehan=dogumyili(2004)
metehan.yazdirma()