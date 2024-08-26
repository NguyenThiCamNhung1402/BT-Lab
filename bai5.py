# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 23:36:17 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
h, m, s= map(int, input("Nhập thời gian dạng hh:mm:ss:").split(":"))
print("Tổng số giây:",(h *3600)+(m *60)+s  )
