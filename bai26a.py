# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:30:45 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
a, b, c = map(int, input("Nhập ba số (cách nhau bởi dấu cách): ").split())
if a > b:
    temp = a
    a = b
    b = temp
if a > c:
    temp = a
    a = c
    c = temp
if b > c:
    temp = b
    b = c
    c = temp
print("Thứ tự tăng dần của 3 số:", a, b, c)