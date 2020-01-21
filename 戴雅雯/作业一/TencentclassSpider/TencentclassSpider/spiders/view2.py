#排名机构供课数量占比图(列举出供课数前十机构
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

f = open("F:/TencentclassSpider/all_info.csv",'rb')
info = pd.read_csv(f)

info = info[['organization','name']]
df = info.groupby('organization')['name'].size().sort_values(ascending=False).head(10)
sum = 0
for i in range(0,10):
    sum += df[i]
num = 9984-sum
df=df.append(pd.Series(num,index=['其他']))
df.name = ''
# 控制饼图为正圆
plt.axes(aspect = 'equal')
# plot方法对序列进行绘图
df.plot(kind = 'pie',title = '排名机构供课数量占比图(列举出供课数前十机构）',autopct = '%.1f%%',radius = 1, startangle = 180,counterclock = False,wedgeprops = {'linewidth': 1.5, 'edgecolor':'green'},textprops = {'fontsize':10, 'color':'black'})
plt.savefig('F:/TencentclassSpider/view2.png')
#plt.show()
