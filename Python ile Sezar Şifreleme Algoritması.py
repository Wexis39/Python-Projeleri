K_alfabe = "abcçdefgğhiıjklmnoöprsştuüvyz"

Bosluk = " "

B_alfabe = K_alfabe.upper()

K_ing_alf = "qwx"
B_ing_alf = "QWX"

alfabe = B_alfabe + K_alfabe + K_ing_alf + B_ing_alf + Bosluk

sezar_atlama = 1

while True:
    mesaj = input("Çıkış yapmak için \"q\" harfine basınız.\nŞifrelemek için 1'i seçiniz\nŞifre kırmak için 2'yi seçiniz\nSeçiminiz: ")

    if mesaj.lower() == 'q':
        break

    Sifrelenmis_index = []

    if mesaj == '1':
        mesaj = input("Şifrelemek istediğiniz mesajı girin: ")
        for index in mesaj:
            if index in alfabe:
                a = ord(index)
                a += sezar_atlama
                b = chr(a)
                Sifrelenmis_index.append(b)

        Sifrelenmis_mesaj = "".join(Sifrelenmis_index)
        print("Şifrelenmiş mesajınız: ", Sifrelenmis_mesaj)

    elif mesaj == '2':
        sifre_coz = input("Çözmek istediğiniz şifreyi girin: ")
        Sifrelenmis_index = []
        for index in sifre_coz:
            if index in alfabe:
                a = ord(index)
                a -= sezar_atlama
                b = chr(a)
                Sifrelenmis_index.append(b)
        Cozulmus_mesaj = "".join(Sifrelenmis_index)
        print("Çözülmüş mesajınız: ", Cozulmus_mesaj)

    else:
        print("Geçersiz seçim. Lütfen 1, 2 veya 'q' girin.")
    break

