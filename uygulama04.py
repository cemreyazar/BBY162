#Soru 1
metin = "Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesini, bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır."
metinn = metin [ :20]
print(metinn)

#Soru 2
liste = ["Açık Bilim", "Açık Erişim", "Açık Lisans", "Açık Eğitim", "Açık Veri", "Açık Kültür"]
for i in liste:
    print(i)

#Soru 3
sozluk = {"Elma" : "Ağaçta yetişen bir tür meyve" , "Salatalık" : "Fidan üzerinde büyüyen bir tür sebze" }
x = input("Bir Kelime Giriniz: ")
if x == "Elma":
    print("Ağaçta yetişen bir tür meyve")
elif x == "Salatalık":
    print("Fidan üzerinde büyüyen bir tür sebze")
else:
    print("Girdiğiniz Kelime Sözlükte Bulunmamaktadır."
