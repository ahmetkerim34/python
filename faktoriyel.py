# -*- coding: utf-8 -*-
"""

FAKTÖRİYEL HESAPLAMA ROBOTU

"""


def hesapla_faktoriyel(number):
    factorial = 1
    if number >= 0:
        for i in range(1, number + 1):
            factorial *= i
        return factorial
    else:
        return None
 
number = int(input("Lütfen faktöriyelini bulmak istediğiniz sayıyı giriniz...\n"))
factorial = hesapla_faktoriyel(number)
 
if factorial:
    print(f"Girdiğiniz sayının faktöriyeli: {number}! = {factorial}")
else:
    print("Negatif sayıların faktöriyeli olmaz!")