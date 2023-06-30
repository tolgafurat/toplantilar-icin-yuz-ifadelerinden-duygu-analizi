import numpy as np
from tensorflow import keras
from keras.models import load_model
import time
from tensorflow.keras.utils import img_to_array
from keras.preprocessing import image
import cv2
from matplotlib import pyplot as plt
from moviepy.editor import VideoFileClip

yuz_siniflandirici = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') ##open cv yüz tespiti dosyası

siniflandirici = keras.models.load_model('model.h5')

duygular = ['Ofkeli','Igrenmis','Korkmus','Mutlu','Sakin', 'Uzgun', 'Saskin']


kayit_adi="video.mp4"
kayit = cv2.VideoCapture(kayit_adi)

duygu_dosyasi = open("Duygular.txt", "w")
zaman_dosyasi = open("Zaman.txt", "w")

## Grafik oluşturmak için gerekli bilgileri txt'ye atıyor
video = VideoFileClip(kayit_adi)
video_suresi = video.duration
videoinfo = open("videoinfo.txt", "w")
videoinfo.write(str(video_suresi))

## uygulama çalışma süresini tutuyoruz
baslangic_zamani = time.time()

## Grafik için gerekli verileri geçici olarak bu dizilerde tutacağız
duygu_listesi =  [0,0,0,0,0,0,0,0,0,0,0]
tekrar_list= [0,0,0,0,0,0,0]
sayac = 0
duygu_ort = [0,0,0,0,0,0,0]


while True:
    kontrol, anlik_kare = kayit.read() ## anlık kare alıyor
    
    for i in range(1, 10):  ## Video fps'ine göre anlık alınan karelerin bir kısmı hesaplamaya dahil edilmiyor (daha hızlı çalışması için)
        kontrol, anlik_kare = kayit.read()

    if kontrol == False:
        break 

    labels = []
    siyah_beyaz = cv2.cvtColor(anlik_kare,cv2.COLOR_BGR2GRAY)
    yuzler = yuz_siniflandirici.detectMultiScale(siyah_beyaz) ## Yüz tespiti

    for (x,y,w,h) in yuzler: ##anlık görüntü üzerinde yüzler için döngü
        cv2.rectangle(anlik_kare,(x,y),(x+w,y+h),(0,255,255),2)
        ilgili_siyah_beyaz_alan = siyah_beyaz[y:y+h,x:x+w]
        ilgili_siyah_beyaz_alan = cv2.resize(ilgili_siyah_beyaz_alan,(48,48),interpolation=cv2.INTER_AREA)

        if sayac == 6: ## çalışma sırasında anlık olmayan yüzlerden gelen yanlış verilerin önüne geçmek ve daha sağlıklı ortalama duygu tespiti için 
            for duygu in duygu_listesi:
                if duygu=="Ofkeli" :
                    tekrar_list[0] += 1
                elif duygu=="Igrenmis":
                    tekrar_list[1] += 1
                elif(duygu=="Korkmus"):
                    tekrar_list[2] += 1
                elif(duygu=="Mutlu"):
                    tekrar_list[3] += 1
                elif(duygu=="Sakin"):
                    tekrar_list[4] += 1
                elif(duygu=="Uzgun"):
                    tekrar_list[5] += 1
                elif(duygu=="Saskin"):
                    tekrar_list[6] += 1
            
            en_cok_tekrarlanan_index = tekrar_list.index(max(tekrar_list))
            duygu_ort[en_cok_tekrarlanan_index] += 1

            if en_cok_tekrarlanan_index == 0 :
                duygu_dosyasi.write("Ofkeli\n")

                anlik_zaman = time.time()
                zaman_dosyasi.write(str(round(anlik_zaman-baslangic_zamani,2))+"\n")

            elif en_cok_tekrarlanan_index == 1:

                duygu_dosyasi.write("Igrenmis\n")

                anlik_zaman = time.time()
                zaman_dosyasi.write(str(round(anlik_zaman-baslangic_zamani,2))+"\n")

            elif(en_cok_tekrarlanan_index == 2):

                duygu_dosyasi.write("Korkmus\n")

                anlik_zaman = time.time()
                zaman_dosyasi.write(str(round(anlik_zaman-baslangic_zamani,2))+"\n")

            elif(en_cok_tekrarlanan_index == 3):

                duygu_dosyasi.write("Mutlu\n")

                anlik_zaman = time.time()
                zaman_dosyasi.write(str(round(anlik_zaman-baslangic_zamani,2))+"\n")

            elif(en_cok_tekrarlanan_index == 4):

                duygu_dosyasi.write("Sakin\n")

                anlik_zaman = time.time()
                zaman_dosyasi.write(str(round(anlik_zaman-baslangic_zamani,2))+"\n")

            elif(en_cok_tekrarlanan_index == 5):

                duygu_dosyasi.write("Uzgun\n")

                anlik_zaman = time.time()
                zaman_dosyasi.write(str(round(anlik_zaman-baslangic_zamani,2))+"\n")

            elif(en_cok_tekrarlanan_index == 6):

                duygu_dosyasi.write("Saskin\n")

                anlik_zaman = time.time()
                zaman_dosyasi.write(str(round(anlik_zaman-baslangic_zamani,2))+"\n")

            ##label_listi sıfırla
            for x in range(len(duygu_listesi)):
                duygu_listesi[x]=0
                
            print("duygu listesi")
            print(duygu_listesi)

            ##tekrar_listi sıfırla
            print(tekrar_list)
            for x in range(len(tekrar_list)):
                tekrar_list[x]=0
  
            print ("en çok tekrarlanan index")
            print (en_cok_tekrarlanan_index)
            
            sayac = 0
        
        
        if np.sum([ilgili_siyah_beyaz_alan]) != 0:
            ilgili_alan = ilgili_siyah_beyaz_alan.astype('float')/255.0
            ilgili_alan = img_to_array(ilgili_alan)
            ilgili_alan = np.expand_dims(ilgili_alan,axis=0)

            tahmin = siniflandirici.predict(ilgili_alan)[0] ## yüz modele gönderilerek modelin çıktısı tespit ediliyor
            duygu = duygular[tahmin.argmax()] ##duygu kaydediliyor

            print(duygu)
            duygu_listesi[sayac]=duygu

            duygu_koordinati = (x,y)
            cv2.putText(anlik_kare,duygu,duygu_koordinati,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        else:
            cv2.putText(anlik_kare,'No Faces',(30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

        sayac += 1
        
        
    cv2.imshow('Duygu Analizi',anlik_kare) ##uygulama penceresi


    if cv2.waitKey(1) & 0xFF == ord('q'): ##çıkış fonksiyonu
        break
    

print("Ortalama duygular listesi")
print(duygu_ort)

with open('Duygu ortalamaları.txt', 'w') as dosya: ##grafikler için veri depolama
    for veri in duygu_ort:
        dosya.write(str(veri) + '\n')

kayit.release()
cv2.destroyAllWindows()