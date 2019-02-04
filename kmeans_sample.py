# -*- coding: utf-8 -*-
# 2次元プロットデータ（3クラス）のデータを読み込んで，k-means法でクラスタリングする
import numpy as np

# 2点間距離を測る関数
def distance(a, b):
    dist = 0.0
    for i in range(len(a)):
        dist += (a[i] - b[i])**2
    dist = np.sqrt(dist)    
    return dist

# データを読み込む
data = np.loadtxt("data.csv", delimiter=",")


val = np.array([2,3])
dist = distance(val, data[0])
print(dist)
