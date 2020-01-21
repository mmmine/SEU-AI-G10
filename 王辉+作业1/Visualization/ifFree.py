#绘制饼状图，按课程是否免费进行分类

import matplotlib.pyplot as plt
import pymysql

#从保存爬虫数据的本地数据库中查询免费课程的数量和课程总数
conn = pymysql.connect(host="localhost",user='root',passwd='apple321',
                      db='keqq',port=3306,use_unicode=True, charset="utf8")
sql_all = 'select count(*) from course_qq'
sql_free = 'select count(*) from course_qq where price=\'免费\''
cursor = conn.cursor()
cursor.execute(sql_all)
result_all = cursor.fetchall()
cursor.execute(sql_free)
result_free = cursor.fetchall()
cursor.close()
conn.close()
freecourse = result_free[0][0]
notfreecourse = result_all[0][0] - result_free[0][0]

plt.rcParams['font.sans-serif'] = 'SimHei'#设置中文显示
plt.figure(figsize=(6,6))#将画布设定为正方形
label=['免费', '收费']#定义饼图的标签
values=[freecourse, notfreecourse]
plt.pie(values, labels=label, autopct='%1.1f%%')#绘制饼图
plt.title('腾讯课堂课程收费情况')#绘制标题
plt.show()