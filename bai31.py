# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:02:39 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
def kt(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Tam giác đều"
        elif a == b or a == c or b == c:
            return "Tam giác cân"
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Tam giác vuông"
        else:
            return "Tam giác khác"
    return "Không phải tam giác"
while True:
    try:
        a, b, c = map(int, input("Nhập ba cạnh (cách nhau bởi dấu cách): ").split())
        if a > 0 and b > 0 and c > 0:
            print(kt(a, b, c))
        else:
            print("Vui lòng nhập các số nguyên dương.")
    except ValueError:
        print("Nhập sai. Thử lại.")
        break
