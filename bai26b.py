# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 21:12:05 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
N = input("Nhập một số nguyên N: ")
d = list(N)
i = 0
while i < len(d) - 1:
    if d[i] > d[i + 1]:
        d[i], d[i + 1] = d[i + 1], d[i]
        i = 0  
    else:
        i += 1
print(''.join(d))
