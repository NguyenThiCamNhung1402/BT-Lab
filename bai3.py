# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 23:29:35 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
if a > 0 and b > 0:
    print("Phần nguyên:",a // b, "Phần dư:",a % b)
else:
    print("Số nhập vào phải là số nguyên dương.")
