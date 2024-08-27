# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:37:38 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
ngay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
try:
    thang = int(input("Nhập số tháng (1-12): "))
    nam = int(input("Nhập số năm: "))
    if 1 <= thang <= 12:
        for i in range(12):
            if thang == i + 1:
                if thang == 2:
                    print("Tháng này có 29 ngày" if (nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0)) else "Tháng này có 28 ngày")
                else:
                    print(f"Tháng này có {ngay[i]} ngày")
                break
    else:
        print("Tháng không hợp lệ. Vui lòng nhập lại.")
except ValueError:
    print("Nhập sai. Thử lại.")
    
