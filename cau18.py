# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:06:24 2024

@author: LENOVO
"""

a1 = int(input("Nhập số giờ 1:"))
b1 = int(input("Nhập số phút 1:"))
c1= int(input("NHập số giây 1:"))
a2 = int(input("Nhập số giờ 2:"))
b2 = int(input("Nhập số phút 2:"))
c2 = int(input("Nhập số giây 2:"))
gio_cong_gio = a1 + a2
gio_tru_gio = a1 - a2
phut_cong_phut = b1 + b2
phut_tru_phut = b1 - b2
giay_cong_giay = c1 + c2
giay_tru_giay = c1 - c2
print("kết quả cộng là:" , gio_cong_gio , "giờ", phut_cong_phut , "phút", giay_cong_giay , "giây")
print("kết quả trừ là:" , gio_tru_gio , "giờ", phut_tru_phut , "phút", giay_tru_giay , "giây")
