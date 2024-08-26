# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 23:43:28 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
import math
a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))
if a == 0 or b == 0: 
    print("Lỗi: a,b không thể bằng 0.")
else:
    can_a, can_b = math.sqrt(a), math.sqrt(b)
    can3_a, can3_b, can3_ab = a ** (1/3), b ** (1/3), (a*b)**(1/3)
    p1 = ((a+b) / (can3_a + can3_b) ) - (can3_ab)
    p2 = (can3_a - can3_b) ** 2
    print("Kết quả biểu thức:",p1 / p2)

