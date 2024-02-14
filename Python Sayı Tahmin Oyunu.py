import random

number = random.randint(0,100)

print("0 ve 100 arasında tahmin yapınız.")

def sonuc():

    if guess < number:
        print("Daha büyük sayı giriniz")
    elif guess > number:
        print("Daha küçük sayı giriniz")
    else:
        print("Tebrikler doğru cevap")

while True:
    guess = int(input("Tahmininiz: "))
    sonuc()
    if guess==number:
        break
