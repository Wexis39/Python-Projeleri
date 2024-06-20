sayi = int(input('sayi: '))

if sayi < 2:
    print(f'{sayi} asal degildir.')
else:
    for i in range(2,sayi):
        if sayi%i==0:
            print(f'{sayi} asal degildir.')
            break
    else:
        print(f'{sayi} asaldir.')