#各价格区间内课程数量图
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

f = open("F:/TencentclassSpider/all_info.csv",'rb')
info = pd.read_csv(f)

classnum0 = info[info.price == 0]['name'].count()
classnum1 = info[(info.price > 0) & (info.price <= 1000)]['name'].count()
classnum2 = info[(info.price > 1000) & (info.price <= 2000)]['name'].count()
classnum3 = info[(info.price > 2000) & (info.price <= 3000)]['name'].count()
classnum4 = info[(info.price > 3000) & (info.price <= 4000)]['name'].count()
classnum5 = info[(info.price > 4000) & (info.price <= 5000)]['name'].count()
classnum6 = info[(info.price > 5000) & (info.price <= 6000)]['name'].count()
classnum7 = info[(info.price > 6000) & (info.price <= 7000)]['name'].count()
classnum8 = info[info.price > 7000]['name'].count()

df = pd.DataFrame({'课程数量':[classnum0,classnum1,classnum2,classnum3,classnum4,classnum5,classnum6,classnum7,classnum8]},index=['免费','1-1000','1001-2000','2001-3000','3001-4000','4001-5000','5001-6000','6001-7000','7000以上'])
y = range(0,7000,500)
df.plot(kind='bar',yticks=y)
for x,y in enumerate([classnum0,classnum1,classnum2,classnum3,classnum4,classnum5,classnum6,classnum7,classnum8]):
    plt.text(x,y,'%d' %y,ha='center')
plt.xlabel('价格区间')
plt.ylabel('课程数量')
plt.title("各价格区间内课程数量图")

plt.savefig('F:/TencentclassSpider/view1.png')
plt.show()