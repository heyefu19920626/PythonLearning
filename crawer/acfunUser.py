import requests
import json



# 用来判断是否后面是否还有用户
is_over = 0 


def get_user_info(uid, user_json):
    """ 得到用户信息 """
    global is_over
    if 'userjson' in user_json.keys():
        user_info = user_json['userjson']
        username = user_info['name']
        lastLoginIp = user_info['lastLoginIp']
        lastLoginDate = user_info['lastLoginDate']
        if 'comeFrom' in user_info.keys():
            comeFrom = user_info['comeFrom']
            print("用户UID:" + str(uid) + " 用户昵称:" + username + " 最近登录IP :" +
                  lastLoginIp + " 最近登录日期:" + lastLoginDate + "来自:" + comeFrom)
        else:
            print('用户UID:' + str(uid), '用户昵称:' + username, '最近登录IP:' +
                  lastLoginIp, '最近登录日期:' + lastLoginDate, ' 来自:' + "未知")
        is_over = 0
    else:
        print('用户UID:' + str(uid), '用户状态:' + user_json['result'])
        if user_json['result'] == '用户不存在null':
            is_over += 1


for i in range(11613821, 11613999):
    # print(is_over)
    if is_over > 100:
        break
    url = "http://www.acfun.cn/usercard.aspx?uid=" + str(i)
    response = requests.get(url)
    jsontext = response.text
    user_json = {}
    try:
        user_json = json.loads(jsontext)
    except:
        print("用户UID:" + str(i) + "请求状态:请求页面错误")

    get_user_info(i, user_json)
