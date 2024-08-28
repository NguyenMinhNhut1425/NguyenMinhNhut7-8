# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:56:56 2024

@author: MINH NHUT
"""
#char = input("Nhập vào một chữ cái hoa hoặc thường: ")
#print(char.swapcase())

#Cấu trúc rẻ nhánh
char = input("Nhập vào một chữ cái hoa hoặc thường: ")
if char.islower():
    chu_hoa = char.upper()
    print(f"{char} là chữ thường đổi thành chữ hoa: {chu_hoa}")
else:
    chu_thuong = char.lower()
    print(f"{char} là chữ hoa đổi thành chữ thường: {chu_thuong}")