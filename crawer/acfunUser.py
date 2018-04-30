import requests
import json
import os

# 用来判断是否后面是否还有用户
is_over = 0
# 用来判断总共获取了多少有效用户
total = 0
# 用来判断文件大小,不超过10M
FILe_SIZE = 10 * 1024 * 1024
# 文件编码个数
file_num = 6
# 写入文件路径
path = "acfun_user_" + str(file_num) + ".json"


def get_user_info(uid, user_json):
    """ 得到用户信息 """
    global is_over
    global total
    global file_num
    global path
    # 如果json串中有用户数据
    if 'userjson' in user_json.keys():
        user_info = user_json['userjson']
        username = user_info['name']
        regTime = user_info['regTime']
        lastLoginIp = user_info['lastLoginIp']
        lastLoginDate = user_info['lastLoginDate']

        if 'comeFrom' in user_info.keys():
            comeFrom = user_info['comeFrom']
        else:
            comeFrom = ''

        user_info = {'UID': uid, 'name': username, 'regTime': regTime,
                     'lastLoginIp': lastLoginIp, 'lastLoginDate': lastLoginDate, 'comeFrom': comeFrom}

        with open(path, 'a', encoding='utf-8') as file:
            json.dump(user_info, file, ensure_ascii=False)
            file.write('\n')
        # 文件大于10M则换文件
        if os.path.getsize(path) < FILe_SIZE:
            pass
        else:
            file_num += 1
            path = "acfun_user_" + str(file_num) + ".json"

        total += 1
        is_over = 0
    else:
        # print('用户UID:' + str(uid), '用户状态:' + user_json['result'])
        if user_json['result'] == '用户不存在null':
            with open('error_log.log', 'a', encoding='utf-8') as file:
                file.write("用户UID:" + str(uid) + "用户状态:" +
                           user_json['result'] + "\n")
        else:
            with open('error_log.log', 'a', encoding='utf-8') as file:
                file.write("用户UID:" + str(uid) + "用户状态:" +
                           user_json['result'] + "\n")
        is_over += 1


start = 719202
while start < 30000000:
    if is_over > 1000:
        break
    url = "http://www.acfun.cn/usercard.aspx?uid=" + str(start)
    try:
        response = requests.get(url)
        jsontext = response.text
    except:
        with open('request_error.log', 'a', encoding='utf-8') as file:
            file.wirte('用户UID:' + str(start) + ' 请求出错')
    user_json = {}
    try:
        user_json = json.loads(jsontext)
    except:
        # print("用户UID:" + str(i) + "请求状态:请求页面错误")
        with open('error_log.log', 'a', encoding='utf-8') as file:
            file.write("用户UID:" + str(start) + "请求状态:请求页面错误\n")
        continue
    get_user_info(start, user_json)
    start += 1

# for i in range(719202, 30000000):
#     # print(is_over)
#     if is_over > 1000:
#         break
#     url = "http://www.acfun.cn/usercard.aspx?uid=" + str(i)
#     try:
#         response = requests.get(url)
#         jsontext = response.text
#     except:
#         with open('request_error.log', 'a', encoding='utf-8') as file:
#             file.wirte('用户UID:' + str(i) + ' 请求出错')
#     user_json = {}
#     try:
#         user_json = json.loads(jsontext)
#     except:
#         # print("用户UID:" + str(i) + "请求状态:请求页面错误")
#         with open('error_log.log', 'a', encoding='utf-8') as file:
#             file.write("用户UID:" + str(i) + "请求状态:请求页面错误\n")
#         continue
#     get_user_info(i, user_json)


with open('total', 'w', encoding='utf-8') as file:
    file.write('总共有' + str(total) + '有效用户')
