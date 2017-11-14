# 功能：从Mysql读取数据
# 例子：to_mysql("select * from database")
import pymysql


def query_mysql(sql): # query SQL语句
    # 打开数据库连接
    db = pymysql.connect("60.30.156.148", "root", "bairiyishanjin", "app_adm", charset="utf8")
    # 使用 cursor() 方法创建一个游标对象 cursor
    # cursor = db.cursor()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute(sql)
        # 提交数据库执行
        db.commit()
    except:
        # 如果有错误回滚
        db.rollback()
        print("数据库查询时发生错误")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    # 关闭数据库连接
    db.close()
    return data
def insert_mysql(sql,list):
    # 打开数据库连接
    db = pymysql.connect("60.30.156.148", "root", "bairiyishanjin", "app_adm", charset="utf8")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # 使用 execute()  方法执行 SQL 查询
        cursor.executemany(sql,list)
        # 提交数据库执行
        db.commit()
        print("数据写入成功！")
    except:
        # 如果有错误回滚
        db.rollback()
        print("数据库写入时发生错误")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    # 关闭数据库连接
    db.close()
    return data
