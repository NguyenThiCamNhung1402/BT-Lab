# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:09:05 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
s = float(input("Nhập số km:"))
tong_tien = 0
if s <= 1:
    tong_tien += 15000
elif 1<s<=5: 
    tong_tien += (s  * 13500)
else:
    tong_tien += (5*13500+(s -5)*11000 )
if s> 120:
    tong_tien *= 0.9
print("Tổng tiền phải trả:",tong_tien,"đồng ")
