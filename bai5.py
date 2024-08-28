# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 12:38:50 2024

@author: MINH NHUT
"""

thoi_gian = input("Nhập giờ, phút, giây theo định dạng hh:mm:ss : ")
gio, phut, giay = map(int, thoi_gian.split(':'))
tong_giay = gio * 3600 + phut * 60 + giay
print(f"{thoi_gian} đổi ra giây là: {tong_giay} giây")