# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:22:17 2024

@author: LENOVO
"""

a = int(input("Nhập số a:"))
b = int(input("Nhập số b:"))
c = int(input("Nhập số c:"))
min_valua = min(a, b, c)
max_valua =max(a, b, c)
mid_valua = a + b + c - min_valua - max_valua
print("Số theo thứ tự tăng dần" , min_valua,mid_valua,max_valua)
N = input("Nhập số nguyên N:")
Sap_xep_N = ''.join(sorted(N))
print("Các con số nguyên theo thứ tự tăng dần là",Sap_xep_N)
