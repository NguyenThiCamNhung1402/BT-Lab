# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:31:04 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
d, m, y = input("Nhập ngày tháng năm sinh (vd 14 2 2005): ").split()
print(f"a) {d}/{m}/{y}")
print(f"b) {d}/{m}/{y[-2:]}")
print(f"c) {y}/{m}/{d}")
n, t, ng = input("Nhập ngày/tháng/năm hoặc năm/tháng/ngày: ").split('/')
if len(n) == 4:
    print(f"Năm/tháng/ngày: {n}/{t}/{ng }")
    print(f"Ngày/tháng/năm: {ng }/{t}/{n}")
else:
    print(f"Ngày/tháng/năm: {n}/{t}/{ng }")
    print(f"Năm/tháng/ngày: {ng }/{t}/{n}")
