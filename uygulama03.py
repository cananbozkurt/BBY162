from random import randint

print("Adam Asmaca Oyununa Hoşgeldiniz")
print("Konu Ankara'daki en iyi üniversiteler")
print("Toplam 4 can hakkınız vardır.")

toplamCan = 4
kelimeler = ["hacettepe","bilkent","odtü","gazi"]
kelimeSayisi = len(kelimeler)
secilen = randint(0, kelimeSayisi-1)
secilenKelime = kelimeler[secilen]
print("secilenKelime")
dizilenKelime = []
for diz in kelimeler[secilen]:
    dizilenKelime.append("_")
    print(dizilenKelime)

while toplamCan > 0 :
    girilenHarf = input("Bir Harf Giriniz: ")
    canKontrol = girilenHarf in secilenKelime
    if canKontrol == False:
        toplamCan-=1
    i = 0
    for kontrol in secilenKelime:
        if secilenKelime[i] == girilenHarf:
            dizilenKelime[i] = girilenHarf
        i+=1
    print(dizilenKelime)
    print("Kalan can: "+ str(toplamCan))

