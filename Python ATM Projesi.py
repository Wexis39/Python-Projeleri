username = "Metehan"
password = "12345"
balance = 5000

log_username = input("Lütfen kullanıcı adınızı giriniz: ")

def login():
    global log_username
    global password
    if log_username == username:
        log_password = input("Lütfen şifrenizi giriniz: ")
        if log_password == password:
            print("Giriş başarılı")
            print("-"*15)
            return True
        else:
            print("Yanlış şifre girdiniz")
            return False
    else:
        print("Kullanıcı adı kayıtlı değil")
        return False


def islemler():
    global draw
    global deposit
    secim =int(input("* Para çekmek için 1\n* Para yatırmak için 2\n* Bakiyeyi görüntülemek için 3\n* Seçiminiz: "))
    global balance
    if secim == 1:
        draw=int(input("Kaç para çekmek istiyorsunuz: "))
        balance-=draw
        print("- çekilen para:",draw)
        print("-"*20)
        return True
    elif secim == 2:
        deposit=int(input("Kaç para yatırmak istiyorsunuz: "))
        balance+=deposit
        print("- Yatırılan para:",deposit)
        print("-"*20)
        return True
    elif secim == 3:
        print("* Bakiyeniz:",balance)
        print("-"*20)
        return True

    else:
        print("Lütfen 1 veya 2'yi seçiniz...")
        return False

if login():
    while True:
        islemler()

