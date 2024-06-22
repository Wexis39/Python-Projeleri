import random

def puanlama():
    global yapayZekaPuan
    global puanin
    yapayZekaPuan = 0
    puanin = 0
    

def yapayZekaSecim():
    global yapayZekaHamlesi
    yapayZekaSecimi = random.randint(1,3)
    if yapayZekaSecimi == 1:
        yapayZekaHamlesi = 'Tas'
    elif yapayZekaSecimi == 2:
        yapayZekaHamlesi = 'Kagit'
    elif yapayZekaSecimi == 3:
        yapayZekaHamlesi = 'Makas'

def secim():
    global seciminiz
    global hamleniz
    print('-'*12)
    seciminiz = input('1-Tas\n2-Kagit\n3-Makas\nSeciminiz: ')
    print('-'*12)
    if seciminiz == '1':
        hamleniz = 'Tas'
        return True
    elif seciminiz == '2':
        hamleniz = 'Kagit'
        return True
    elif seciminiz == '3':
        hamleniz = 'Makas'
        return True
    else:
        print('Gecerli bir secim yapiniz.')
        return False

def kimKazandi():
    global yapayZekaPuan
    global puanin
    if hamleniz == 'Tas':
        if yapayZekaHamlesi == 'Tas':
            print(f'* Botun hamlesi {yapayZekaHamlesi.upper()} Beraberlik!')
            print(f'PUAN DURUMU: Sen: {puanin} Bot: {yapayZekaPuan}')
        elif yapayZekaHamlesi == 'Kagit':
            print(f'* Botun hamlesi {yapayZekaHamlesi.upper()} Kaybettiniz!')
            yapayZekaPuan+=1
            print(f'PUAN DURUMU: Sen: {puanin} Bot: {yapayZekaPuan}')
        elif yapayZekaHamlesi == 'Makas':
            print(f'* Botun hamlesi {yapayZekaHamlesi.upper()} Kazandiniz!')
            puanin+=1
            print(f'PUAN DURUMU: Sen: {puanin} Bot: {yapayZekaPuan}')
    elif hamleniz == 'Kagit':
        if yapayZekaHamlesi == 'Tas':
            print(f'* Botun hamlesi {yapayZekaHamlesi.upper()} Kazandiniz!')
            puanin+=1
            print(f'PUAN DURUMU: Sen: {puanin} Bot: {yapayZekaPuan}')
        elif yapayZekaHamlesi == 'Kagit':
            print(f'* Botun hamlesi {yapayZekaHamlesi.upper()} Beraberlik!')
            print(f'PUAN DURUMU: Sen: {puanin} Bot: {yapayZekaPuan}')
        elif yapayZekaHamlesi == 'Makas':
            print(f'* Botun hamlesi {yapayZekaHamlesi.upper()} Kaybettiniz!')
            yapayZekaPuan+=1
            print(f'PUAN DURUMU: Sen: {puanin} Bot: {yapayZekaPuan}')
    elif hamleniz == 'Makas':
        if yapayZekaHamlesi == 'Tas':
            print(f'* Botun hamlesi {yapayZekaHamlesi.upper()} Kaybettiniz!')
            yapayZekaPuan+=1
            print(f'PUAN DURUMU: Sen: {puanin} Bot: {yapayZekaPuan}')
        elif yapayZekaHamlesi == 'Kagit':
            print(f'* Botun hamlesi {yapayZekaHamlesi.upper()} Kazandiniz!')
            puanin+=1
            print(f'PUAN DURUMU: Sen: {puanin} Bot: {yapayZekaPuan}')
        elif yapayZekaHamlesi == 'Makas':
            print(f'* Botun hamlesi {yapayZekaHamlesi.upper()} Beraberlik!')
            print(f'PUAN DURUMU: Sen: {puanin} Bot: {yapayZekaPuan}')


print('-'*12)
print('3 puan olan kazanir.')


puanlama()
while True:
    yapayZekaSecim()
    if secim():
        kimKazandi()
        if puanin >= 3:
            print('-'*12)
            print(f'Oyunu {puanin} - {yapayZekaPuan} KAZANDINIZ !')
            print('-'*12)
            quit()
        elif yapayZekaPuan >= 3:
            print('-'*12)
            print(f'Oyunu {yapayZekaPuan} - {puanin} KAYBETTINIZ !')
            print('-'*12)
            quit()