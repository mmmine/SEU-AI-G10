import pandas as pd
from matplotlib import pyplot

data = pd.read_csv("../class.csv")
name=[]
number=[]
for index in range(len(data)):
    name.append(data["name"][index])
    number.append(data["Number of people purchased"][index])
res={}
for index in range(len(number)):
    res["{}".format(name[index])]=int(number[index])
ret=sorted(res.items(), key=lambda item:item[1], reverse=True)
resName=[]
resNumber=[]
for i in range(20):
    resName.append(ret[i][0])
    resNumber.append(ret[i][1])

pyplot.figure(figsize=(20,8),dpi=80)
#.bar()是绘制条形图，注意这里传的第一个参是range(len(film))，因为绘图参数得传数字，想要显示名字得最后通过设置x、y轴一一对应;但经测验直接传film也可以
pyplot.barh(range(len(resName)),resNumber,height=0.3)
pyplot.ylabel("courseName")
pyplot.xlabel("number")
pyplot.title("购买人数排名前20的课程")
pyplot.yticks(range(len(resName)),resName)
pyplot.savefig('../analysis.png')
pyplot.show()