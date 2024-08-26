# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:26:34 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
a, b, c, d = map(int, input("Nhập 4 số nguyên (cách nhau bằng khoảng trắng): ").split())
m = a
m = (b if b < m else m)
m = (c if c < m else m)
m = (d if d < m else m)
print("Số nhỏ nhất:", m)
