# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:12:41 2024

@author: MINH NHUT
"""

a = float(input("Nhập vào giá trị của a: ")) 
b = float(input("Nhập vào giá trị của b: ")) 
p_t = f"Phương trình bậc nhất {a}x + {b} = 0"
if a == 0:
    if b == 0:
        print(f"{p_t} có vô số nghiệm")
    else:
        print(f"{p_t} vô nghiệm")
else:
    x = (-b) / a
    print(f"{p_t} có nghiệm x = {x}")