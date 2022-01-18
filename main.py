import random
import time

class Kumanda():
    def __init__(self, tv_durum = "Kapalı", tv_ses = 0, kanal_listesi = ["TRT"], kanal = "TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if(self.tv_durum == "Açık"):
            print("Televizyon zaten açık.")
        else:
            self.tv_durum = "Açık"
            print("Televizyon açıldı.")

    def tv_kapat(self):
        if(self.tv_durum == "Kapalı"):
            print("Televizyon zaten kapalı.")
        else:
            self.tv_durum = "Kapalı"
            print("Televizyon kapandı.")

    def ses_ayari(self):
        print("Şu anki ses: ", self.tv_ses)

        while(True):

            cevap = input("Sesi Artır: >\nSesi Azalt: <\nÇıkış: 'q'\n")
            if(cevap == ">"):
                if(self.tv_ses == 31):
                    print("Maksimum ses düzeyine ulaşıldı.")
                if(self.tv_ses != 32):
                    self.tv_ses +=1
                    print("Ses artırıldı: ",self.tv_ses)
            elif(cevap == "<"):
                if (self.tv_ses == 0):
                    print("Minimum ses düzeyine ulaşıldı.")
                if(self.tv_ses != 0):
                    self.tv_ses -=1
                    print("Ses azaltıldı: ",self.tv_ses)
            elif(cevap == "q"):
                print("Ses güncellendi: ",self.tv_ses)
                print("Çıkış yapılıyor . . .")
                break
            else:
                print("Hatalı tuşlama yapıldı.")

    def kanal_ekle(self, kanal):

        print("Kanal ekleniyor . . .")
        time.sleep(1)

        self.kanal_listesi.append(kanal)
        print("Kanal eklendi")

    def rastgele_kanal(self):

        rastgele_sayi = random.randint(0, len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele_sayi]
        print("Şu anki kanal: ", self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "TV Durum: {}\nTV Ses: {}\nKanal Listesi: {}\nŞu anki Kanal: {}".format(self.tv_durum, self.tv_ses,self.kanal_listesi, self.kanal)


kumanda = Kumanda()
print("""
Televizyon Uygulaması

1. TV AÇ

2. TV KAPAT

3. SES AYARLARI

4. KANAL EKLE

5. KANAL SAYISINI ÖĞRENME

6. RASTGELE KANALA GEÇME

7. TELEVİZYON BİLGİLERİ

Çıkmak için 'q' ya basınız
""")

while(True):
    islem = input("İşlemi seçiniz: ")
    if(islem == "q"):
        print("Program sonlandırılıyor . . .")
        break

    elif(islem == "1"):
        kumanda.tv_ac()
    elif(islem == "2"):
        kumanda.tv_kapat()
    elif(islem == "3"):
        kumanda.ses_ayari()
    elif(islem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' (virgül) ile ayırarak yazınız.")
        kanal_listesi = kanal_isimleri.split(",")

        for i in kanal_listesi:
            kumanda.kanal_ekle(i)
    elif(islem == "5"):
        print("Kanal sayısı: ",len(kumanda))
    elif(islem == "6"):
        kumanda.rastgele_kanal()
    elif(islem == "7"):
        print(kumanda)
    else:
        print("Geçersiz işlem")