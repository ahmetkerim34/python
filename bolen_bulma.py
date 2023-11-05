#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TAM BÖLEN BULMA ROBOTU
"""

sayi = int(input("hangi sayının bölenlerini bulalım? > "))
     
for i in range(1,sayi+1):
       if sayi % i == 0:
            print(i)

