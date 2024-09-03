# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:32:59 2024

@author: LENOVO
"""

a = int(input("Nhập số nguyên a:"))
b = int(input("Nhập số nguyên b:"))
tong = a + b
hieu = a - b
tich = a * b
if b != 0:
    thuong_lam_tron_2_chu_so = round(a / b, 2)
    thuong_lam_tron_3_chu_so = round(a / b, 3)
else:
    thuong_lam_tron_2_chu_so = "Không thể chia hết cho 0"
    thuong_lam_tron_3_chu_so = "Không thể chia hết cho 0"
print("tổng của 2 số:" , tong)
print("hiệu của 2 số:" , hieu)
print("tích của 2 số:" , tich)
print("Thương làm tròn 2 chữ số:" , thuong_lam_tron_2_chu_so)
print("Thương làm tròn 3 chữ số:" , thuong_lam_tron_3_chu_so)

