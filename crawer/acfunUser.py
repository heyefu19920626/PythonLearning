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
        regTime = user_info['regTime']
        lastLoginIp = user_info['lastLoginIp']
        lastLoginDate = user_info['lastLoginDate']
        if 'comeFrom' in user_info.keys():
            comeFrom = user_info['comeFrom']
        else:
            comeFrom = ''

        user_info = {'UID': uid, 'name':username, 'regTime': regTime, 'lastLoginIp':lastLoginIp, 'lastLoginDate':lastLoginDate, 'comeFrom': comeFrom}
        print(user_info)
        with open('acfun_user.json', 'a', encoding='utf-8') as file:
            json.dump(user_info, file, ensure_ascii=False)

        is_over = 0
    else:
        # print('用户UID:' + str(uid), '用户状态:' + user_json['result'])
        if user_json['result'] == '用户不存在null':
            is_over += 1


for i in range(1, 10):
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
        # print("用户UID:" + str(i) + "请求状态:请求页面错误")
        continue

    get_user_info(i, user_json)
