# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:00:10 2024

@author: MINH NHUT
"""

a = int(input("Nhập vào số nguyên a: "))
b = int(input("Nhập vào số nguyên b: "))
c = int(input("Nhập vào số nguyên c: "))
d = int(input("Nhập vào số nguyên d: "))
if a < b:
    b = a
if b < c:
    c = b
if c < d:
    d = c
print(f"Số nhỏ nhất là: {d}")