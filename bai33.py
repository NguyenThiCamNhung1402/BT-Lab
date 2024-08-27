# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:48:44 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
import math
n = int(input("Nhập số nguyên dương n: "))
if n > 0 and int(math.sqrt(n)) ** 2 == n:
   print(f"{n} là số chính phương.")
else:
   print(f"{n} không phải là số chính phương.")
