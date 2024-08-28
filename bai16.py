# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:19:08 2024

@author: MINH NHUT
"""

thoi_gian = input("Nhập vào thời gian giờ (h) phút (p) giây (s) (..h..p..s): ")
so = ""
for i in thoi_gian:
    if i.isalpha():
        so += ":"
    else:
        so += i
final_so = so[:-1]
h, p, s = map(int, final_so.split(':'))
giay = h * 3600 + p * 60 + s
print(f"{thoi_gian} đổi thành {giay} giây")
