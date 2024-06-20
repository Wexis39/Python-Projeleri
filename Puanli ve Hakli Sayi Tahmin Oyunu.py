import random

hak = int(input('Hakkin: '))
print('-'*12)
i = 0
puan = 100
puanSistemi = round(puan / hak)
randomSayi = random.randint(1,100)
while i < hak:
    cevap = int(input(f'{hak} hakkiniz var. Cevabin: '))
    if cevap == randomSayi:
        print('-'*12)
        print('--Tebrikler--')
        print('Puaniniz: {}'.format(puan))
        break
    elif cevap < randomSayi:
        print('Daha buyuk bir sayi giriniz.')
        puan = puan - puanSistemi
        print('Puaniniz: {}'.format(puan))
        print('-'*12)
        hak-=1
    elif randomSayi < cevap:
        print('Daha kucuk bir sayi giriniz.')
        puan = puan - puanSistemi
        print('Puaniniz: {}'.format(puan))
        print('-'*12)
        hak-=1
    if hak == i:
        print('Hakkiniz bitti.')
        print('Dogru cevap: {}'.format(randomSayi))
        print('Puaniniz: {}'.format(puan))
        print('-'*12)