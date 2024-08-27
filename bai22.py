# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 12:36:39 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
a=float(input("Nhập giá trị của a:"))
b=float(input("Nhập giá trị của b:"))
if a==0 and b==0:
    print("Phương trình vô số nghiệm")
elif a==0 and b!=0:
    print("Phương trình vô nghiệm")
else:
    x=-b/a
    print("Nghiệm của phương trình",x)
