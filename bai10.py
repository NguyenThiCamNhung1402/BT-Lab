# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:05:41 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
def tao(n):
    while n >= 10:
        n = sum(int(i) for i in str(n))
    return n
so_xe = input("Nhập biển số xe có 4 chữ số: ")
kq = tao(sum(int(i) for i in so_xe))
print("Kết quả cuối cùng là:",kq)
