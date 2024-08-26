# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:05:41 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
def count(so_xe ):
    so_nut  = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1]
    return sum(so_nut [int(i )] for i  in so_xe )
so_xe  = input("Nhập số xe của bạn (4 chữ số): ")
print("Số xe của bạn có" , count(so_xe ), "nút.")
