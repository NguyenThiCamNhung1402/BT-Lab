# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:14:30 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
n = int(input("Nhập một số nguyên: "))
ds = ["Không ", "Một ", "Hai ", "Ba", "Bốn ", "Năm ", "Sáu ", "Bảy ", "Tám ", "Chín "]
print(ds[n] if 0 <= n <= 9 else "Không đọc được")