# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:27:37 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
h, m, s = map(int, input("Nhập giờ, phút, giây (hh mm ss): ").split())
if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
    print("Thời gian hợp lệ")
else:
    print("Thời gian không hợp lệ")
