# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 23:43:28 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
import math
a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))
if b == 0:
    print("Lỗi: b không thể bằng 0.")
else:
    sqrt_a, sqrt_b = math.sqrt(a), math.sqrt(b)
    fourth_root_a, fourth_root_b = a ** 0.25, b ** 0.25
    p1 = (sqrt_a - sqrt_b) / (fourth_root_a - fourth_root_b) if fourth_root_a != fourth_root_b else float('inf')
    p2 = (sqrt_a + (a * b) ** 0.25) / (fourth_root_a + fourth_root_b)
    print("Kết quả biểu thức:",p1 - p2)
    print("Căn bậc 4 của b:",fourth_root_b)
