# -*- coding: utf-8 -*-
# 2次元プロットデータ（3クラス）のデータを読み込んで表示する
import numpy as np
import matplotlib.pyplot as plt

# データを読み込む
data = np.loadtxt("data.csv", delimiter=",")

# データをプロット
plt.scatter(data[:,0], data[:,1], color='b', marker='o', s=20)

# グリッド表示
plt.grid(True)

# 表示
plt.show()
