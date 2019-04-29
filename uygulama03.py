__author__ = "Cemre Yazar"
print("Adam Asmaca Oyununa Hoşgeldiniz !")
print("Bulmanız gereken kelimeler hayvan isimlerinden oluşmaktadır.")

import random
kelimeler=("fil","dinozor","panda","tavşan","zebra",)
secilenKelime=random.choice(kelimeler)
kelimealani=[]
if secilenKelime== "fil":
    print("Hortumlarını, koku alırken veya herhangi bir cismi tutarken kullanırlar.")
if secilenKelime== "dinozor":
    print("İlk çağlarda yaşammış, boyu yirmi metreyi bulabilen, uzun kuyruklu, iri gövdeli, uzun boyunlu.")
if secilenKelime=="panda":
    print("Çin’de bambu ormanlarında yaşayan, siyah beyaz renkli, soyu tükenmek üzere olduğu için koruma altına alınmış yabanıl bir hayvan.")
if secilenKelime=="tavşan":
    print("Çok hızlı,genellikle zıplayarak koşan,eti ve postu için avlanan,memeli bir kemirgen hayvan.")
if secilenKelime=="zebra":
    print("Derisi pijama giymiş gibi tümüyle yol yol çizgili olan memeli hayvan.")

arananHarf=0
kalanCan=5
for hayvan in secilenKelime:
    kelimealani.append("_")
print(kelimealani)
while kalanCan > 0:
    girilenHarf = input("bir harf giriniz:").lower()
    i = girilenHarf in secilenKelime
    if i == False:
        kalanCan -= 1
        print("Girilen harf yanlış. Tekrar deneyin. Kalan can: " + str(kalanCan))
    if kalanCan == 0:
        print('Maalesef kaybettiniz. Doğru kelime "{}"'.format(secilenKelime))

    if girilenHarf in secilenKelime:
        for hayvan in secilenKelime:
            if secilenKelime[arananHarf] == girilenHarf:
                kelimealani[arananHarf] = girilenHarf
            arananHarf += 1
        print(kelimealani)
        arananHarf = 0
    if "_" not in kelimealani:
        print("Tebrikler oyunu kazandınız!")
        break
