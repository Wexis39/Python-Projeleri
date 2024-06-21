while True:
    print('-'*12)
    print('1-Sifrele\n2-Sifre Cozme\n3-Cikis')
    secim = input('Seciminiz: ')
    print('-'*12)
    if secim == '1':
        sifrele = input('Sifrelemek istediginiz mesaj: ')
        sifreliString = ''
        for karakter in sifrele:
            sifreliRakam = ord(karakter)
            sifreliRakam+=3
            sifreliKarakter = chr(sifreliRakam)
            sifreliString+=sifreliKarakter
        print(f'Sifreli mesajiniz: {sifreliString}')
    if secim == '2':
        sifreCoz = input('Sifresini cozmek istediginiz mesaj: ')
        sifresizString = ''
        for karakter in sifreCoz:
            sifresizRakam = ord(karakter)
            sifresizRakam-=3
            sifresizKarakter = chr(sifresizRakam)
            sifresizString+=sifresizKarakter
        print(f'Sifresiz mesajiniz: {sifresizString}')
    if secim == '3':
        print('Cikis yaptiniz.')
        break