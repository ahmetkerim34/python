#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ÖĞRENCİ OTOMASYONUNA HOŞ GELDİNİZ
"""
dosya=open("ogrencibilgileri.txt")

ogrenci_adı=[]
ogrenci_soyadı=[]
ogrenci_sinifi=[]
ogrenci_yasi=[]
ogrenci_cinsiyeti=[]

def ogrenciekle():
    ogrencinin_adı=input("İsim giriniz:")
    ogrencinin_soyadı=input("Soyisim giriniz:")
    ogrencinin_sinifi=int(input("Sınıf giriniz:"))
    ogrencinin_yasi=int(input("Yaş giriniz:"))
    cinsiyet=input("Cinsiyet giriniz:")
    ogrenci_adı.append(ogrencinin_adı)
    ogrenci_soyadı.append(ogrencinin_soyadı)
    ogrenci_sinifi.append(ogrencinin_sinifi)
    ogrenci_yasi.append(ogrencinin_yasi)
    ogrenci_cinsiyeti.append(cinsiyet)
    print("Kayıt işlemi gerçekleşti.")
def ogrencisil():
    ogrencinin_adı=input("İsim giriniz:")
    ogrencinin_soyadı=input("Soyisim giriniz:")
    ogrencinin_sinifi=int(input("Sınıf giriniz:"))
    ogrencinin_yasi=int(input("Yaş giriniz:"))
    cinsiyet=input("Cinsiyet giriniz:")
    ogrenci_adı.append(ogrencinin_adı)
    ogrenci_soyadı.append(ogrencinin_soyadı)
    ogrenci_sinifi.append(ogrencinin_sinifi)
    ogrenci_yasi.append(ogrencinin_yasi)
    ogrenci_cinsiyeti.append(cinsiyet)
    print("Öğrenci kaydı silindi.")
    
def ogrenciarama():
    print("Öğrenci arama seçildi.")
    
def ogrencilistele():
    print("Öğrenci listele seçildi.")
    
    for sn in range(len(ogrenci_adı)):
        print(f"{ogrenci_adı[sn]} {ogrenci_soyadı[sn]} {ogrenci_sinifi[sn]} {ogrenci_yasi[sn]} {ogrenci_cinsiyeti[sn]}")
    
def guncelleme():
    print("Güncelleme seçildi.")
    
def kalanogrenci():
    print("Kalan öğrenci listele seçildi.")
    
def gecenogrenci():
    print("Geçen öğrenci listele seçildi.")
    


def kayit():
    fonksiyonListesi=[ogrenciekle,ogrencisil,ogrenciarama,ogrencilistele,guncelleme,kalanogrenci,gecenogrenci]
    while True:
        print("1-Öğrenci ekle")
        print("2-Öğrenci sil")
        print("3-Öğrenci arama")
        print("4-Öğrenci listele")
        print("5-Güncelleme")
        print("6-Kalan Öğrencileri listele")
        print("6-Geçen Öğrencileri listele")
        print("0-Programdan çık")
        sec=int(input("Lütfen yapmak istediğiniz işlemi seçiniz (0-7):"))
        print("\n"*5)
        if sec<=7 and sec>=1:
            fonksiyonListesi[sec-1]()
            print("Geçerli işlem seçildi.")
        elif sec==0:
            print("Sistemden çık.")
            break
        else:
            print("Lütfen 0 ile 7 arası bir rakam giriniz.")
        
kayit()