# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:24:27 2024

@author: LENOVO
"""

can_nang = float(input("Nhập cân nặng (kg):"))
chieu_cao = float(input("Nhập chiều cao (m):"))
BMI = can_nang / chieu_cao ** 2
print("Số đo kiểm tra sức khỏe BMI là:" , BMI)