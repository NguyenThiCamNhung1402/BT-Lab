# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 12:36:50 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
a=float(input("Nhập giá trị của a:"))
if a==0:
    a=float(input("a phải khác 0, mời nhập lại:"))
b=float(input("Nhập giá trị của b:"))
if b==0:
    b=float(input("b phải khác 0, mời nhập lại:"))
c=float(input("Nhập giá trị của c:"))
delta=b**2-4*a*c
if delta<0:
    print("Phương trình vô nghiệm")
elif delta==0:
    print("Phương trình có nghiệm kép: x1=x2",-(b/2*a))
else:
    print("Phương trình có 2 nghiệm phân biệt:","x1=", (-(b)+ ((delta)**1/2)/(2*a),"x2=", (-(b) - ((delta)**1/2)/(2*a)))) 

