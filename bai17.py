# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:55:35 2024

@author: MINH NHUT
"""

a = int(input("Nhập vào số nguyên thứ nhất: "))
b = int(input("Nhập vào số nguyên thứ hai: "))
c = int(input("Nhập vào số nguyên thứ ba: "))
so_lon_nhat = max(a, b, c)
so_nho_nhat = min(a, b, c)
print("Số lớn nhất là: ", so_lon_nhat)
print("Số nhỏ nhất là: ", so_nho_nhat)