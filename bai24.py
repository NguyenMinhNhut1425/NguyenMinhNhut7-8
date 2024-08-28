# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:47:13 2024

@author: MINH NHUT
"""

gio_phut_giay = input("Nhập vào giờ, phút, giây (hh:mm:ss): ")
gio, phut, giay = map(int, gio_phut_giay.split(':'))
if (0 <= gio <= 24) and (0 <= phut <= 60) and (0 <= giay <=60):
    print(f"{gio_phut_giay} là hợp lệ")
else:
    print(f"{gio_phut_giay} không hợp lệ")