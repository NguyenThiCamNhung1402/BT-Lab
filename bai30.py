# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:37:38 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
thang = int(input("Nhập số tháng: "))
nam = int(input("Nhập số năm: "))
if(thang == 1 or thang ==  3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12):
    print("Tháng này có 31 ngày")
elif(thang == 4 or thang == 6 or thang == 9):
    print("Tháng này có 30 ngày")
elif(thang == 2):
    if(nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0)):
        print("Tháng này có 29 ngày")
    else:
        print("Tháng này có 28 ngày")
else:
    print("Nhập chưa đúng")
    
