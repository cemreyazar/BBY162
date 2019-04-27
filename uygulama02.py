__author__="Cemre Yazar"
print("***Genel kültürünüz ne kadar iyi? Aşağıdaki testle kendinizi denemeye ne dersiniz?***")
print("Hadi başlayalım...")
sorular = ['İlk Çağ uygarlıklarından hangisi yazıyı icat etmiştir?',
           'Tsunamide en fazla zarar gören Güney Asya ülkesi aşağıdakilerden hangisidir?',
           'Hangisi Dünya Sağlık Örgütünün kısaltılmış halidir?',
           'Bir sebepten dolayı tek kulağına küpe takan Osmanlı padişahı kimdir?',
           '2003 yılında Eurovision yarışmasında ülkemizi temsil eden ve birinci olan sanatçı kimdir?']

cevaplar = ['C','A','C','B','D']
cevapA = ['Hititler','Endonezya','UHW','Kanuni Sultan Selim','Athena']
cevapB = ['Elamlar','Srilanka','UNICEF','Yavuz Sultan Selim','Can Bonomo']
cevapC = ['Sümerler','Tayland','WHO','Orhan Bey','Şebnem Paker']
cevapD = ['Urartular','Hindistan','NATO','Fatih Sultan Mehmet','Sertab Erener']

puan = 0
for i in range(len(sorular)):
    print("Soru " + str(i+1)+":"+sorular[i])
    print("A.) " + cevapA[i])
    print("B.) " + cevapB[i])
    print("C.) " + cevapC[i])
    print("D.) " + cevapD[i])
    cevap = input("Cevabınızı Giriniz: ")
    if cevaplar[i] == cevap.upper():
        puan +=1
print("Testi Tamamladınız")
print("Aldığınız not: " +str(int((puan/len(sorular))*100)))
input()
