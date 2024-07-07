import numpy as np


def tongji(data, mistake):
    # 假设 data 是你的数据数组
    data = data

    # 找到数据的最小值和最大值
    min_value = np.min(data)
    max_value = np.max(data)

    # 设置区间范围
    bins = np.arange(min_value, max_value + mistake, mistake)

    # 使用 np.histogram() 统计频数
    hist, _ = np.histogram(data, bins=bins)

    # 打印各个区间的频数
    for i in range(len(hist)):
        lower_bound = bins[i]
        upper_bound = bins[i + 1]
        count = hist[i]
        print(f"区间 [{lower_bound}, {upper_bound}) 中的频数为：{count}")
