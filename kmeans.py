# -*- coding: utf-8 -*-
# 2次元プロットデータ（3クラス）のデータを読み込んで，k-means法でクラスタリングする
import numpy as np

# データを表示する
import matplotlib.pyplot as plt
import matplotlib.cm as cm


# numpyの乱数シード値を固定
np.random.seed(1)

# 2点間距離を測る関数
def distance(a, b):
    dist = 0.0
    for i in range(len(a)):
        dist += (a[i] - b[i])**2
    dist = np.sqrt(dist)
    return dist

# クラスタの重心を求める
def means(cluster) :
    len_cluster = len(cluster)
    len_center = len(cluster[0])
    center = np.zeros([len_center])

    temp = np.array(cluster).T
    for i in range(len_center):
        center[i] = sum(temp[i])/len_cluster

    return center

# k-means法を用いてクラスタリングする
def k_means(data,val,*,times=1000,size=0,fig_name=''):
    data = list(data).copy()
    val = list(val).copy()
    len_data = len(data)
    len_val = len(val)
    count = 1
    old_val = val.copy()

    if (size > 0):
        split = int(times/(size*size))


    # 試行回数：TIMES
    for t in range(times):
        cluster = [[] for i in range(len_val)]

        # 全データと代表点との距離を求め，クラスタの中に分類する
        for i in range(len_data):
            dist = []
            for j in range(len_val):
                dist.append(distance(val[j], data[i]))
            cluster[dist.index(min(dist))].append(data[i])

        # クラスタをプロット
        if (size > 0):
            if (size==1):
                if (t==times-1):
                    for i in range(len_val):
                        temp = np.array(cluster[i]).T
                        plt.scatter(temp[0], temp[1], color=cm.hsv(i/len_val), marker='o', s=10)
                        plt.scatter(val[i][0], val[i][1], color=cm.cool(i/len_val), marker='x', s=100)

            elif (times<=size*size or t%split==0):
                for i in range(len_val):
                    temp = np.array(cluster[i]).T
                    plt.subplot(size,size,count)
                    plt.scatter(temp[0], temp[1], color=cm.hsv(i/len_val), marker='o', s=10)
                    plt.scatter(val[i][0], val[i][1], color=cm.cool(i/len_val), marker='x', s=100)
                count += 1

            # タイトル
            plt.title("t="+str(t))

            # グリッド表示
            plt.grid(True)


        # 新しいクラスタの代表点を求める
        for i in range(len_val):
            val[i] = means(cluster[i])

    # 表示
    if (size > 0):
        # タイトルの被りを防ぐ
        plt.tight_layout()

        if (fig_name == '') :
            plt.show()
        else :
            plt.savefig(fig_name)

    return val


# データを読み込む
data = np.loadtxt("data.csv", delimiter=",")

# 求めるクラスタ数
k = 3

# 乱数で最初のクラスタ重心点を求める
rand_max = 1
rand_min = 0.5
val = np.random.random((k,2))
val += rand_min
val = rand_max - val

# 画像で保存
fig = "k-means.eps"
val = k_means(data,val,times=4,size=2,fig_name=fig)
