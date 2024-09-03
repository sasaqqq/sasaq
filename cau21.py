# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:04:04 2024

@author: LENOVO
"""

number_to_string = {0: "không" , 1: "một" , 2: "hai" , 3: "ba" , 4: "bốn" , 5: "năm" , 6: "sáu" , 7: "bảy" , 8: "tám" , 9: "chín"}
a = int(input("Nhập 1 số bất kì:"))
if 0 <= a <= 9:
    print("chữ số" , number_to_string[a])
else:
    print("Không đọc được")