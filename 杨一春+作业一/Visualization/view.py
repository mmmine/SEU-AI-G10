import pandas
import matplotlib
import matplotlib.pyplot as mpl



matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False


table = pandas.read_csv('course.csv', usecols = ['cname', 'number'])

df = table.sort_values(by = 'number', ascending = False)
df = df.iloc[0:10]
#print(df)


ax = df.plot(kind = 'bar', rot = 90, figsize = (16, 16))
mpl.title('报名人数最多的十个课程', fontsize = 25)


ax.set_xlabel('课程名', fontsize = 20)
ax.legend('', fontsize = 20)
ax.set_ylim(9800, 10000)

mpl.xticks(range(10), list(df['cname']), fontsize = 10)
mpl.yticks(fontsize = 20)

mpl.show()
mpl.savefig('333.png')


	