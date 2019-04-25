puan = 0
print("Atatürk hangi yılda doğdu? ")
cevap = int(input("Cevabınızı Giriniz: "))

if (cevap == 1881):
    print("Tebrikler, cevabınız doğru!")
    puan = puan+20
else:
    print("Yanlış cevap.")

print("Atatürk hangi yılda başkomutan olmuştur? ")
cevap = int(input("Cevabınızı Giriniz: "))

if (cevap == 1921):
    print("Tebrikler, cevabınız doğru!")
    puan = puan+20
else:
    print("Yanlış cevap.")

print("Cumhuriyet ne zaman ilan edildi? ")
cevap = int(input("Cevabınızı giriniz: "))

if (cevap == 1923):
    print("Tebrikler, cevabınız doğru!")
    puan = puan+20
else:
    print("Yanlış cevap.")

print("Atatürk kaç yıl cumhurbaşkanlığı yapmıştır? ")
cevap = int(input("Cevabınızı giriniz: "))

if (cevap == 15):
    print("Tebrikler, cevabınız doğru!")
    puan = puan+20
else:
    print("Yanlış cevap.")

print("Atatürk kaç yaşında vefat ettmiştir? ")
cevap = int(input("Cevabınızı giriniz: "))

if (cevap == 57):
    print("Tebrikler, cevabınız doğru!")
    puan = puan+20
else:
    print("Yanlış cevap.")

print("Aldığınız Toplam Puan =" , puan)
