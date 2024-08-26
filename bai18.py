# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:08:00 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
from datetime import timedelta
h1, m1, s1 = map(int, input("Nhập giờ, phút, giây cho khoảng thời gian 1 (hh mm ss): ").split())
h2, m2, s2 = map(int, input("Nhập giờ, phút, giây cho khoảng thời gian 2 (hh mm ss): ").split())
t1 = timedelta(hours=h1, minutes=m1, seconds=s1)
t2 = timedelta(hours=h2, minutes=m2, seconds=s2)
print("Tổng:", t1 + t2)
print("Hiệu:", abs(t1 - t2))
