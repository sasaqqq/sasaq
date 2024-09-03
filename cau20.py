# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:57:05 2024

@author: LENOVO
"""

a = int(input("Nhập số nguyên a:"))
b = int(input("Nhập số nguyên b:"))
c = int(input("Nhập số nguyên c:"))
if a >= b and a >= c:
    so_gia_tri_lon_nhat = a
elif b >= a and b >= c:
    so_gia_tri_lon_nhat = b
else:
    so_gia_tri_lon_nhat = c
print("Số có giá trị lớn nhất là:" , so_gia_tri_lon_nhat)