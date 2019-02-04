# -*- coding: utf-8 -*-
# 2次元プロットデータ（3クラス）を作成する
import numpy as np


# numpyの乱数シード値を固定
np.random.seed(1)

# 各データの個数
NUM = 30

# クラスター中心
cluster1 = [0,0]
cluster2 = [0.5,0.5]
cluster3 = [0,1]

# データを正規乱数で生成
x1 = np.random.normal(cluster1[0], 0.2, NUM)
y1 = np.random.normal(cluster1[1], 0.2, NUM)

x2 = np.random.normal(cluster2[0], 0.3, NUM)
y2 = np.random.normal(cluster2[1], 0.1, NUM)

x3 = np.random.normal(cluster3[0], 0.15, NUM)
y3 = np.random.normal(cluster3[1], 0.15, NUM)

# データを結合
xx = []
xx.extend(x1)
xx.extend(x2)
xx.extend(x3)
yy = []
yy.extend(y1)
yy.extend(y2)
yy.extend(y3)
data = np.c_[xx, yy]

# ファイル出力
np.savetxt("data.csv", data, delimiter=",",fmt='%10.4f')

# データを表示する
import matplotlib.pyplot as plt

# データをプロット
plt.scatter(x1, y1, color='b', marker='o', s=20)
plt.scatter(x2, y2, color='r', marker='o', s=20)
plt.scatter(x3, y3, color='g', marker='o', s=20)

#plt.scatter(xx, yy, color='b', marker='o', s=20)

# グリッド表示
plt.grid(True)

# 表示
plt.show()
