import pymysql


def getConn():
    return pymysql.connect('localhost', 'root', '123456', 'tencentcourse')


def getQueryList(sql):
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute(sql)
    info = cursor.fetchall()
    return info


def getCategory():
    sql = "select * from categories"
    category = getQueryList(sql)
    for item in category:
        yield item[0], item[2]


sql = "select * from categories"
category = getQueryList(sql)






