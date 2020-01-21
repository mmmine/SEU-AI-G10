import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt


def plot(category_name, top_num):
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False

    """
    绘制水平条形图方法barh
    参数一：y轴
    参数二：x轴
    """
    plt.barh(range(10), top_num, height=0.5, color='steelblue', alpha=1)  # 从下往上画
    plt.yticks(range(10), category_name)
    plt.xlim(min(top_num) - 1000, max(top_num) + 1000)
    plt.xlabel("报名人数")
    plt.title("各个分类报名人数前10的课程")
    for x, y in enumerate(top_num):
        plt.text(y + 0.2, x - 0.1, '%s' % y)
    plt.show()


# 读取数据
data = pd.read_csv("C:/Users/twili/Desktop/course.csv")

# 去重
data.drop_duplicates("course_name",keep='first',inplace=True)

# 分组
data_grouped = data.groupby("category")

# 排序
sorted_list = []
for item in data_grouped:
    list = item[1].sort_values(by="course_num", ascending=False)
    sorted_list.append(list.values)

# 每个分类的前10名
for li in sorted_list:
    cate = np.array(li)
    top_num = cate[:, 6].tolist()[:10]
    category_name = cate[:, 2].tolist()[:10]
    plot(category_name, top_num)


