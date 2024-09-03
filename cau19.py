# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:35:31 2024

@author: LENOVO
"""

a = int(input("Nhập số nguyên a:"))
b = int(input("Nhập số nguyên b:"))
c = int(input("Nhập số nguyên c:"))
d = int(input("Nhập số nguyên d:"))
if a <= b and a <= c and a <= d:
    so_gia_tri_nho_nhat = a
elif b <= a and b <= c and b <= d:
    so_gia_tri_nho_nhat = b
elif c <= a and c <= b and c <= d:
    so_gia_tri_nho_nhat = c
else:
    so_gia_tri_nho_nhat = d
print("Số có giá trị nhỏ nhất là:" , so_gia_tri_nho_nhat)