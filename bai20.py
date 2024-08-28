# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:09:10 2024

@author: MINH NHUT
"""

a = float(input("Nhập vào số nguyên a: "))
b = float(input("Nhập vào số nguyên b: "))
c = float(input("Nhập vào số nguyên c: "))
if a > b:
    b = a
if b > c:
    c = b
print(f"Số lớn nhất là: {c}")