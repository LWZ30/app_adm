import ToMysql
import filecache

keys = ToMysql.query_mysql("select * from proj_av join projects on projects.proj_id = proj_av.proj_id join attributes on attributes.av_id = proj_av.av_id");
keyMap = {}
for key in keys:
    keyMap[key['proj_av_id']] = key

@filecache(60)
def user_profile(user_id):
    data = ToMysql.query_mysql("select * from proj_av where usr_id = '{0}'".format(user_id))
    user = {}
    for item in data:
        proj_name = keyMap[item['proj_av_id']]['proj_name']
        av_name = keyMap[item['proj_av_id']]['av_name']
        if proj_name not in user:
            user[proj_name] = {}
        user[proj_name][av_name]=item['value']
    return user

@filecache(60)
def project_users(proj_id):
    data = ToMysql.query_mysql("select usr_id from users "
                               "join proj_av on proj_av.proj_av_id = users.proj_av_id "
                               "where proj_av.proj_id = {0}".format(proj_id))
    result = []
    for item in data:
        result.append(user_profile(item['usr_id']))

    return result

p = project_users(1)
print(p)