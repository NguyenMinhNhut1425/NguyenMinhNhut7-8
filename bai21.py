# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:49:42 2024

@author: MINH NHUT
"""

so = int(input("Nhập một số bất kỳ: "))
doc = {0:'Không', 1:'Một', 2:'Hai', 3:'Ba', 4:'Bốn', 5:'Năm', 6:'Sáu', 7:'Bảy', 8:'Tám', 9:'Chín'}
if so >= 0 and so <= 9:
    chuso = doc.get(so)
    print(chuso)
else:
    print("Không đọc được")