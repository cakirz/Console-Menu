#Bu kod Mert Bülbül (220502006) ve Can Şafak Çakır (220502002) tarafından hazırlanmıştır.

import math
from functools import reduce


def k_kucuk():
    def k_küçük(int, liste):
        if int > len(liste):
            return min(liste)

        sıralı_liste = sorted(liste)
        kucuk_eleman = sıralı_liste[int - 1]
        return kucuk_eleman

    def main():
        try:
            sayı_gir = input("Bir sayı girin: ")

            if not sayı_gir.isdigit():
                raise ValueError("Lütfen geçerli bir sayı girin.")

            sayı = int(sayı_gir)
            if sayı <= 0:
                raise ValueError("k değeri pozitif tam sayı olmalıdır.")

            liste = [int(x) for x in input("Listeyi sayıların arasında boşluk olacak şekilde giriniz: ").split()]

            if len(liste) == 0:
                raise ValueError("Liste boş olamaz.")

            sonuc = k_küçük(sayı, liste)
            print(f"En küçük {sayı}. eleman: {sonuc}")

        except ValueError as e:
            print(f"Hata: {e}")
            if str(e).startswith("Lütfen geçerli bir sayı girin.") or str(e).startswith("Liste boş olamaz."):
                main()
            else:
                return

    if __name__ == "__main__":
        main()
#------------------------------------------------------------------------------------------------------------------#
def en_yakin_çift():
    def en_yakin_cift(int, liste):
        liste.sort()
        en_yakin = None
        en_kucuk_fark = float('inf')

        for i in range(len(liste) - 1):
            for j in range(i + 1, len(liste)):
                toplam = liste[i] + liste[j]
                fark = abs(int - toplam)

                if fark < en_kucuk_fark:
                    en_kucuk_fark = fark
                    en_yakin = (liste[i], liste[j])

        return en_yakin

    def main():
        try:
            hedef_sayi = int(input("İstediğniz hedef sayıyı girin: "))
            liste = [int(x) for x in input("Listeyi sayıların arasında boşluk olacak şekilde giriniz: ").split()]

            sonuç = en_yakin_cift(hedef_sayi, liste)

            print(f"girdiğiniz {hedef_sayi} sayısına en yakın çift: {sonuç[0]} ve {sonuç[1]}")

        except ValueError:
            print("Hatalı giriş! Lütfen geçerli bir tam sayı girin.")
            main()

    if __name__ == "__main__":
        main()
#------------------------------------------------------------------------------------------------------------------#
def tekrar_eden_sayi():
    def tekrar_eden_sayi(liste):
        tekrar_edenler = [eleman for eleman in liste if liste.count(eleman) > 1]
        return list(set(tekrar_edenler))

    def main():
        try:
            liste = [int(x) for x in input("Listeyi sayıların arasında boşluk olacak şekilde giriniz: ").split()]

            sonuc = tekrar_eden_sayi(liste)

            if not sonuc:
                print("Tekrar eden sayı yok. Listeyi tekrar giriniz.")
                main()
            else:
                print("Tekrar eden sayı:", sonuc)

        except ValueError:
            print("Hatalı giriş! Lütfen geçerli bir tam sayı girin.")
            main()

    if __name__ == "__main__":
        main()
#------------------------------------------------------------------------------------------------------------------#
def matris_çarpımı():
    def matris_carpimi(liste1, liste2):
        if len(liste1[0]) != len(liste2):
            return "Hatalı matris. İlk matrisin sütun sayısı, ikinci matrisin satır sayısına eşit olamaz lütfen tekrar girin."

        sonuc = [[sum(ele1 * ele2 for ele1, ele2 in zip(row1, col2)) for col2 in zip(*liste2)] for row1 in liste1]
        return sonuc

    def main():
        birincinin_satir_sayisi = int(input("Birinci matrisin satır sayısını girin: "))
        matris1 = []
        for _ in range(birincinin_satir_sayisi):
            satir = [int(x) for x in input("Birinci matrisin satırını boşluklarla ayırarak girin: ").split()]
            matris1.append(satir)

        ikincinin_satir_sayisi = int(input("İkinci matrisin satır sayısını girin: "))
        matris2 = []
        for _ in range(ikincinin_satir_sayisi):
            satir = [int(x) for x in input("İkinci matrisin satırını boşluklarla ayırarak girin: ").split()]
            matris2.append(satir)

        sonuç = matris_carpimi(matris1, matris2)
        print("\nÇarpım Matrisi:")
        for row in sonuç:
            print(row)

    if __name__ == "__main__":
        main()
#------------------------------------------------------------------------------------------------------------------#
def frekans_bul():
    def frekans_bul(dosya_konumu):
        with open(dosya_konumu, 'r') as dosya:
            metin = dosya.read()

        kelimeler = metin.split()


        frekanslar = reduce(
            lambda frekanslar, kelime: frekanslar.update({kelime: frekanslar.get(kelime, 0) + 1}) or frekanslar,
            kelimeler, {})

        return frekanslar

    dosya_konumu = str(input("Dosya Konumu Girin"))
    frekanslar = frekans_bul(dosya_konumu)

    for kelime, frekans in frekanslar.items():
        print(f"{kelime}={frekans}")
#-----------------------------------------------------------------------------------------------------------------#
def en_kucuk_deger():
    def en_kucuk_değer(liste):
        if not liste:
            return None

        eleman = liste[0]

        ikinci_en_kucuk = en_kucuk_değer(liste[1:])

        if ikinci_en_kucuk is not None and ikinci_en_kucuk < eleman:
            return ikinci_en_kucuk
        else:
            return eleman

    def main():
        while True:
            liste = [int(x) for x in input("Listeyi sayıların arasında boşluk olacak şekilde giriniz: ").split()]

            if not liste:
                print("Liste boş , lütfen değerleri tekrar giriniz.")
                continue

            en_kucuk = en_kucuk_değer(liste)

            if en_kucuk is not None:
                print(f"En küçük eleman: {en_kucuk}")
                break
            else:
                print("Birden fazla en küçük eleman bulunmakta . değerleri tekrar giriniz.")

    if __name__ == "__main__":
        main()
#----------------------------------------------------------------------------------------------------------------#
def karekok():
    print()
    print()
    print("#####  Bu Hizmet  mevcut değil  #####")
    print()
    print()
#-----------------------------------------------------------------------------------------------------------------#
def ebob():
    def ebob(sayi1, sayi2):
        if sayi2 == 0:
            return sayi1
        else:
            return ebob(sayi2, sayi1 % sayi2)

    def main():
        sayi1 = int(input("Birinci sayıyı girin: "))
        sayi2 = int(input("İkinci sayıyı girin: "))

        sonuc = ebob(sayi1, sayi2)
        print(f"{sayi1} ve {sayi2} sayılarının ebobu: {sonuc}")

    if __name__ == "__main__":
        main()
#------------------------------------------------------------------------------------------------------------------#
def asal_test():
    def asal_veya_değil(sayı):
        if sayı <= 1:
            return False
        if sayı == 2:
            return True
        if sayı % 2 == 0:
            return False
        for i in range(3, int(sayı ** 0.5) + 1, 2):
            if sayı % i == 0:
                return False
        return True

    def main():
        sayı = int(input("Bir sayı girin: "))

        if asal_veya_değil(sayı):
            print(f"{sayı} bir asal sayıdır.")
        else:
            print(f"{sayı} bir asal sayı değildir.")
            main()

    if __name__ == "__main__":
        main()
#------------------------------------------------------------------------------------------------------------------#
def hizli_fibonacci():
    print()
    print()
    print("#####  Bu Hizmet  mevcut değil  #####")
    print()
    print()
#------------------------------------------------------------------------------------------------------------------#
def cikis():
    print("Çıkışınız yapılıyor ...")
    exit()
#-------------------------------------------------------------------------------------------------------------------#
def konsol():
    konsol_calistir = {
        1: ("K. En Küçük Eleman", k_kucuk,),
        2: ("En Yakın Çift Sayı", en_yakin_çift),
        3: ("Listenin Tekrar Eden Elemanları ", tekrar_eden_sayi),
        4: ("Matris Çarpımı ", matris_çarpımı),
        5: ("Kelimelerin Frekansı", frekans_bul),
        6: ("Listedeki En Küçük Değer", en_kucuk_deger),
        7: ("Karekök Fonksiyonu ", karekok),
        8: ("Ebob ", ebob),
        9: ("Asallık Testi ", asal_test),
        10: ("Hızlı Fibonacci Hesabı ", hizli_fibonacci),
        0: ("çıkış", cikis)
    }

    while True:
        print("Konsol Menüsü:")
        for secenekler, işlem in konsol_calistir.items():
            print(f"{secenekler}: {işlem[0]}")

        secim = int(input("İstediğiniz işlemi girin: "))

        if secim in konsol_calistir:
            konsol_calistir[secim][1]()
        else:
            print("Geçerli bir seçenek girin")

konsol()
