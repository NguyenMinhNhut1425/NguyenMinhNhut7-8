# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:04:40 2024

@author: MINH NHUT
"""

from datetime import datetime
nam_sinh = int(input("Nhập vào năm sinh: "))
nam_nay = datetime.now().year
tuoi = nam_nay - nam_sinh
print(f"Bạn sinh năm {nam_sinh}, năm nay là {nam_nay} vậy bạn được {tuoi} tuổi")