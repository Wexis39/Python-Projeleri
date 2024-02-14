import time


class isci:
    def __init__(self, isim = "Tanımlanmadı", yas = "Tanımlanmadı" , meslek = "Tanımlanmadı"):
        self.isim = isim
        self.yas = yas
        self.meslek = meslek

    def yazdırma(self):
        print("YAZDIRILIYOR...")
        time.sleep(3)
        print("isim:",self.isim,"\nyas:",self.yas,"\ngorev:",self.meslek)
        print("-"*18)

isci1 = isci(input("isim: "),input("yas: "),input("meslek: "))
isci2 = isci()

isci1.yazdırma()
isci2.yazdırma()



