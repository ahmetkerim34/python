#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aranan Nokta Alanın İçinde Mi?
"""

x1=int(input("noktanın x değerini giriniz:"))
y1=int(input("noktanın y değerini giriniz:"))

taban=int(input("üçgenin taban değerini giriniz:"))
yükseklik=int(input("üçgenin yükseklik değerini giriniz:"))

x2=int(input("üçgenin sol alt x değerini giriniz:"))
y2=int(input("üçgenin sol alt y değerini giriniz:"))


cnt=0

if(x1>x2 and x1<x2+taban):
    cnt+=1
if(y1>y2 and y1<y2+yükseklik):
    cnt+=1
    
if(cnt==2):
    print("nokta alanın içinde")
else:
    print("nokta alanın içinde değil")