# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 22:06:07 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
N = int(input("Nhập số nguyên dương N: "))
if N <= 0:
    print("Số nhập vào không hợp lệ!")
else:
    print("Các ước số của", N, "là:")
    for i in range(1, N + 1):
        if N % i == 0:
            print(i)
