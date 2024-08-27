# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 21:24:08 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
import math
s = input("Nhập loại hình (v: hình vuông, n: hình chữ nhật, t: hình tròn): ").lower()
if s == 'v':
    c = float(input("Nhập chiều dài cạnh hình vuông: "))
    P, S = 4 * c , c * c 
elif s == 'n':
    w = float(input("Nhập chiều rộng hình chữ nhật: "))
    l = float(input("Nhập chiều dài hình chữ nhật: "))
    P, S = 2 * (w + l), w * l
elif s == 't':
    r = float(input("Nhập bán kính hình tròn: "))
    P, S = 2 * math.pi * r, math.pi * r * r
else:
    print("Loại hình không hợp lệ!")
    exit()
print("Kết quả: P =", round(P, 2), ", S =", round(S, 2))

