# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:23:17 2024

@author: MINH NHUT
"""

import math
a = float(input("Nhập vào giá trị của a: "))
b = float(input("Nhập vào giá trị của b: "))
c = float(input("Nhập vào giá trị của c: "))
p_t = f"Phương trình bậc hai {a}x\u00B2 + {b}x + c = 0"
delta = (b ** 2) - (4 * a * c)
if delta < 0:
    print(f"{p_t} vô nghiệm")
elif delta == 0:
    x = (-b) / (2 * a)
    print(f"{p_t} có nghiệm kép x1 = x2 = {x}")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"{p_t} có hai nghiệm phân biệt x1 = {x1} và x2 = {x2}")