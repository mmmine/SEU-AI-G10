#绘制直方图，显示拥有课程数量最多的培训机构

import matplotlib.pyplot as plt
import pymysql

#从保存爬虫数据的本地数据库中查询各机构的课程数量
conn = pymysql.connect(host="localhost",user='root',passwd='apple321',
                      db='keqq',port=3306,use_unicode=True, charset="utf8")
sql = 'select count(*),agency from course_qq group by agency'
cursor = conn.cursor()
cursor.execute(sql)
result = cursor.fetchall()
cursor.close()
conn.close()
agency_sorted = sorted(result, reverse=True)#按课程数量降序排列，此处数据类型为元组

name_list = []#x轴，机构名称
num_list = []#y轴，机构拥有的课程数量
for i in range(10):
	name_list.append(agency_sorted[i][1])
	num_list.append(agency_sorted[i][0])#取课程数量前十的机构

plt.rcParams['font.sans-serif'] = 'SimHei'#设置中文显示
rects=plt.bar(range(len(num_list)), num_list, color='rgby')
index=[0, 1 , 2, 3, 4, 5, 6, 7, 8, 9]
index=[float(c)+0.4 for c in index]
plt.ylim(ymax=200, ymin=50)
plt.xticks(index, name_list)
plt.ylabel("课程数量")
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha='center', va='bottom')
plt.title('腾讯课堂课程拥有量最高的十家机构')#绘制标题
plt.show()