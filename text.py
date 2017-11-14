import FromExcel # 自定义模块读取excel文件
import ToMysql # 自定义模块
import uuid # 唯一标识码模块

data_av=ToMysql.query_mysql("select proj_av_id,av_name from v_proj_av where proj_id=2")
# 查找属性对应的proj_av_id
def search_av(data,sear):
    for v in data:
       if(sear in v):
           return str(v[0])

data = FromExcel.from_excel("无线网管理员.xlsx")
# 获取属性列表
av=data[0]
# 循环数据行
tmp = []
for row in data[1:]:
    usr_id=str(uuid.uuid1())
    for item in row[1:]:
        proj_av_id=search_av(data_av,av[row.index(item)])
        av_value=str(item)
        tmp.append((usr_id,proj_av_id,av_value))
keep_going=input("是否确认导入数据库？ y/n : ")
if keep_going=='y':
    ToMysql.insert_mysql("insert into users (usr_id,proj_av_id,av_value) VALUES (%s,%s,%s)",tmp)
else:
    print(tmp)

