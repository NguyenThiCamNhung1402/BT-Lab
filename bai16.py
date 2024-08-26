# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 12:29:18 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
time = input("Nhập thời gian (vd 2h10p5s): ")
if 'h' in time and 'p' in time and 's' in time:
    h, m, s = map(int, time.replace("h", " ").replace("p", " ").replace("s", " ").split())
    print("Tổng số giây:", h * 3600 + m * 60 + s)
else:
    print("Chuỗi đầu vào không đúng định dạng. Vui lòng nhập lại theo định dạng '2h10p5s'.")
