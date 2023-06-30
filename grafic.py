import matplotlib.pyplot as plt
import numpy as np
duygular = ['Öfkeli','İğrenmiş','Korkmuş','Mutlu','Sakin', 'Üzgün', 'Şaşkın']

## PASTA GRAFİK
# Dosyadan veri okuma
with open('Duygu ortalamaları.txt', 'r') as dosya:
    veri = dosya.read().splitlines()
    print(veri)
# Veriyi diziye dönüştürme
veri_dizisi = list(map(int, veri))

# Veri dizisini kullanma
print(veri_dizisi)

renkler = ['#ff6666', '#468499', '#ff7f50', '#ffdab9', 
          '#00ced1', '#ffff66','#088da5']
sekil, eksenler = plt.subplots(figsize=(14,7))

eksenler.pie(veri_dizisi,labels=duygular,colors=renkler, 
        autopct='%1.1f%%');

plt.show()

##NOKTA GRAFİK
#Öncül veri hazırlığı
ofke_degerleri = []
with open('Duygular.txt', 'r') as dosya1:
    duygu_listesi = dosya1.read().splitlines()
    for duygu in duygu_listesi:
        if duygu == "Ofkeli" :
            ofke_degerleri.append(1)
        else:
            ofke_degerleri.append(-1)
print(ofke_degerleri)


igrenme_degerleri = []
with open('Duygular.txt', 'r') as dosya1:
    duygu_listesi = dosya1.read().splitlines()
    for duygu in duygu_listesi:
        if duygu == "Igrenmis" :
            igrenme_degerleri.append(2)
        else:
            igrenme_degerleri.append(-1)
print(igrenme_degerleri)

korku_degerleri = []
with open('Duygular.txt', 'r') as dosya1:
    duygu_listesi = dosya1.read().splitlines()
    for duygu in duygu_listesi:
        if duygu == "Korkmus" :
            korku_degerleri.append(3)
        else:
            korku_degerleri.append(-1)
print(korku_degerleri)


mutlu_degerleri = []
with open('Duygular.txt', 'r') as dosya1:
    duygu_listesi = dosya1.read().splitlines()
    for duygu in duygu_listesi:
        if duygu == "Mutlu" :
            mutlu_degerleri.append(4)
        else:
            mutlu_degerleri.append(-1)
print(mutlu_degerleri)



sakin_degerleri = []
with open('Duygular.txt', 'r') as dosya1:
    duygu_listesi = dosya1.read().splitlines()
    for duygu in duygu_listesi:
        if duygu == "Sakin" :
            sakin_degerleri.append(5)
        else:
            sakin_degerleri.append(-1)
print(sakin_degerleri)



uzgunluk_degerleri = []
with open('Duygular.txt', 'r') as dosya1:
    duygu_listesi = dosya1.read().splitlines()
    for duygu in duygu_listesi:
        if duygu == "Uzgun" :
            uzgunluk_degerleri.append(6)
        else:
            uzgunluk_degerleri.append(-1)
    
print(uzgunluk_degerleri)



saskinlik_degerleri = []
with open('Duygular.txt', 'r') as dosya1:
    duygu_listesi = dosya1.read().splitlines()
    for duygu in duygu_listesi:
        if duygu == "Saskin" :
            saskinlik_degerleri.append(7)
        else:
            saskinlik_degerleri.append(-1)
    
print(saskinlik_degerleri)



with open('Zaman.txt', 'r') as dosya2:
    zaman = dosya2.read().splitlines()

zaman = list(map(float, zaman))


with open('videoinfo.txt', 'r') as dosya3:
    video_suresi_listesi = dosya3.read().splitlines()
video_suresi_listesi = list(map(float, video_suresi_listesi))

video_suresi=video_suresi_listesi[0]

print("Video uzunluğu:", video_suresi, "saniye")

a=video_suresi/len(zaman)

print(a)
suredizisi=[]
suredizisi.append(0)

for i in range(len(zaman)-1):
    b = round(suredizisi[i]+a,2)
    suredizisi.append(b)


print(len(suredizisi))
print(suredizisi)



print(len(zaman))
print(zaman)

y_eksen= [1, 2, 3, 4, 5, 6,7]

##NOKTA GRAFİK
# Grafik oluşturma
plt.scatter(suredizisi, ofke_degerleri, label='Öfkeli')
plt.scatter(suredizisi, igrenme_degerleri, label='İğrenmiş')
plt.scatter(suredizisi, korku_degerleri, label='Korkmuş')
plt.scatter(suredizisi, mutlu_degerleri, label='Mutlu')
plt.scatter(suredizisi, sakin_degerleri, label='Sakin')
plt.scatter(suredizisi, uzgunluk_degerleri, label='Üzgün')
plt.scatter(suredizisi, saskinlik_degerleri, label='Şaşkin')

plt.yticks(y_eksen, duygular)

# Eksen etiketlerini ayarlama
plt.xlabel('ZAMAN(sn)')
plt.ylabel('DUYGULAR')

# Grafik başlığını ayarlama
plt.title('Duygu - Zaman grafiği')
# Y-ekseni sınırlarını ayarlama
plt.ylim([0, 8])


l1=np.arange(0,video_suresi,1)
plt.xticks(l1)
# Grafiği gösterme
plt.show()


y_ekseni2= [0,1, 2]
##ÇİZGİ GRAFİK

#Öfke duygusu
# Grafik oluşturma
plt.plot(suredizisi, ofke_degerleri, label='Öfke - Zaman Grafiği')
# Eksen etiketlerini ayarlama
plt.xlabel('ZAMAN(sn)')
plt.ylabel('Öfke Duygu Durumu')

# Grafik başlığını ayarlama
plt.title('Öfke - Zaman Grafiği')
# Y-ekseni sınırlarını ayarlama
plt.ylim([0, 2])

plt.xticks(l1)
plt.legend()

#Eksen adlarını değiştirme
y_ekseni2= [0,1, 2]
Durum_dizi=["Yok","Var"," "]
plt.yticks(y_ekseni2, Durum_dizi)

# Grafiği gösterme
plt.show()


##İğrenme duygusu 
# Grafik oluşturma
plt.plot(suredizisi, igrenme_degerleri, label='İğrenme - Zaman Grafiği')

# Eksen etiketlerini ayarlama
plt.xlabel('ZAMAN')
plt.ylabel('İğrenme Duygu Durumu')

# Grafik başlığını ayarlama
plt.title('İğrenme - Zaman Grafiği')
# Y-ekseni sınırlarını ayarlama
plt.ylim([0, 4])
plt.xticks(l1)
plt.legend()

y_ekseni2= [0,1, 2, 3 ,4 ]
Durum_dizi=["Yok"," ","Var"," "," "]
plt.yticks(y_ekseni2, Durum_dizi)

# Grafiği gösterme
plt.show()

##Korku duygusu
# Grafik oluşturma
plt.plot(suredizisi, korku_degerleri, label='Korku - Zaman Grafiği')

# Eksen etiketlerini ayarlama
plt.xlabel('ZAMAN(sn)')
plt.ylabel('Korku Duygu Durumu')

# Grafik başlığını ayarlama
plt.title('Korku - Zaman Grafiği')
# Y-ekseni sınırlarını ayarlama
plt.ylim([0, 6])

plt.xticks(l1)
# Şeritleri gösterme

plt.legend()


y_ekseni2= [0,1, 2, 3 ,4,5,6 ]
Durum_dizi=["Yok"," "," ","Var"," "," "," "]
plt.yticks(y_ekseni2, Durum_dizi)


# Grafiği gösterme
plt.show()


# Grafik oluşturma
plt.plot(suredizisi, mutlu_degerleri, label='Mutluluk - Zaman Grafiği')

# Eksen etiketlerini ayarlama
plt.xlabel('ZAMAN(sn)')
plt.ylabel('Mutluluk Duygu Durumu')

# Grafik başlığını ayarlama
plt.title('Mutluluk - Zaman Grafiği')
# Y-ekseni sınırlarını ayarlama
plt.ylim([0, 8])

plt.xticks(l1)

# Şeritleri gösterme
plt.legend()


y_ekseni2= [0,1, 2, 3 ,4,5,6,7,8 ]
Durum_dizi=["Yok"," "," "," ","Var"," "," "," "," "]
plt.yticks(y_ekseni2, Durum_dizi)

# Grafiği gösterme
plt.show()

# Grafik oluşturma
plt.plot(suredizisi, sakin_degerleri, label='Sakinlik - Zaman Grafiği')

# Eksen etiketlerini ayarlama
plt.xlabel('ZAMAN(sn)')
plt.ylabel('Sakinlik Duygu Durumu')

# Grafik başlığını ayarlama
plt.title('Sakinlik - Zaman Grafiği')
# Y-ekseni sınırlarını ayarlama
plt.ylim([0, 10])

plt.xticks(l1)

# Şeritleri gösterme
plt.legend()

y_ekseni2= [0,1,2,3,4,5,6,7,8,9,10]
Durum_dizi=["Yok"," "," "," "," ","Var"," "," "," "," "," "]
plt.yticks(y_ekseni2, Durum_dizi)


# Grafiği gösterme
plt.show()

# Grafik oluşturma
plt.plot(suredizisi, uzgunluk_degerleri, label='Üzgünlük - Zaman Grafiği')

# Eksen etiketlerini ayarlama
plt.xlabel('ZAMAN(sn)')
plt.ylabel('Üzgünlük Duygu Durumu')

# Grafik başlığını ayarlama
plt.title('Üzgünlük - Zaman Grafiği')
# Y-ekseni sınırlarını ayarlama
plt.ylim([0, 12])

plt.xticks(l1)

# Şeritleri gösterme
plt.legend()


y_ekseni2= [0,1,2,3,4,5,6,7,8,9,10,11,12]
Durum_dizi=["Yok"," "," "," "," "," ","Var"," "," "," "," "," "," "]
plt.yticks(y_ekseni2, Durum_dizi)

# Grafiği gösterme
plt.show()

# Grafik oluşturma
plt.plot(suredizisi  , saskinlik_degerleri, label='Şaşkınlık - Zaman Grafiği')

# Eksen etiketlerini ayarlama
plt.xlabel('ZAMAN(sn)')
plt.ylabel('Şaşkınlık Duygu Durumu')

# Grafik başlığını ayarlama
plt.title('Şaşkınlık - Zaman Grafiği')
# Y-ekseni sınırlarını ayarlama
plt.ylim([0, 14])

plt.xticks(l1)

# Şeritleri gösterme
plt.legend()


y_ekseni2= [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
Durum_dizi=["Yok"," "," "," "," "," "," ","Var"," "," "," "," "," "," "," "]
plt.yticks(y_ekseni2, Durum_dizi)

# Grafiği gösterme
plt.show()

