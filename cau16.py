# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:05:30 2024

@author: LENOVO
"""

gio = int(input("Nhập giờ:"))
phut = int(input("Nhập phút:"))
giay = int(input("Nhập giây:"))
tong_so_giay = gio * 3600 + phut * 60 + giay
print("Tổng số giây là:" , tong_so_giay)