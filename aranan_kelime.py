#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cümle İçerisinde Kelime Arama
"""

metin = "Sessiz bir sonbahar gecesiydi.Hava serin ve bulutluydu.Annem ve babam Kayseriye gittiği için evde yalnızdım.Arkadaşlarımla serbestçe eğlenmenin tam zamanıydı..."


aranan_kelime = input("aranacak kelimeyi giriniz:").lower()
kelime = ""

for i in range(0,len(metin)):
    for j in range(0,len(metin) - i):
        
        kelime += metin[i+j].lower()
        if len(kelime) == len(aranan_kelime):
            if kelime == aranan_kelime:
                print("Kelime bulundu.")
                
                
            
            kelime = ""
            break