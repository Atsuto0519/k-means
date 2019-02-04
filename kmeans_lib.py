import numpy as np
from sklearn.cluster import KMeans

# データを読み込む
data = np.loadtxt("data.csv", delimiter=",")

# k-meansクラスタリング
kmeans_model = KMeans(n_clusters=3, random_state=10).fit(data)

# 分類先となったラベルを取得する
labels = kmeans_model.labels_

# ラベルを表示する
for label, dat in zip(labels, data):
    print(label, dat)


# プロットする
import matplotlib.pyplot as plt

for i in range(len(data)):
    if labels[i]==0:
        plt.scatter(data[i,0], data[i,1], color='r', marker='o', s=20)
    elif labels[i]==1:
        plt.scatter(data[i,0], data[i,1], color='g', marker='o', s=20)
    else:
        plt.scatter(data[i,0], data[i,1], color='b', marker='o', s=20)
        
# グリッド表示
plt.grid(True)

# 表示
plt.show()
