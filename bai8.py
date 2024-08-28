# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:13:01 2024

@author: MINH NHUT
"""

nang = float(input("Nhập vào cân nặng (kg): "))
cao = float(input("Nhập vào chiều cao (m): "))
bmi = nang / (cao ** 2)
print(f"Số đo sức khỏe BMI của bạn là: {bmi}")