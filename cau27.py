# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:48:01 2024

@author: LENOVO
"""

hinh = input("Nhập vào hình vuông(v),chữ nhật(n),tròn(t):")
if hinh == 'v':
    canh = float(input("Nhập chiều dài cạnh hình vuông:"))
    chu_vi = 4*canh
    print("Chu vi hình vuông là:" , chu_vi)
    dien_tich = canh**2
    print("Diện tích hình vuông là:" , dien_tich)
elif hinh == 'n':
    chieu_rong = float(input("Nhập chiều rộng của hình chữ nhật:"))
    chieu_dai = float(input("Nhập chiều dài của hình chữ nhật:"))
    chu_vi = 2 * chieu_rong + chieu_dai
    print("Chu vi hình chữ nhật là:" , chu_vi)
    dien_tich = chieu_rong * chieu_dai
    print("Diện tích hình chữ nhật là:" ,dien_tich)
elif hinh == 't':
    ban_kinh = float(input("Nhập bán kính hình tròn:"))
    chu_vi = 2 * 3.14 * ban_kinh
    print("Chu vi hình tròn là: " , chu_vi)
    dien_tich = 3.14*(ban_kinh**2)
    print("Diện tích hình tròn là: " , dien_tich)
else:
    print("Không xác định")