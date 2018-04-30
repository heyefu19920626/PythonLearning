import requests
import re
import hashlib


password = 'admin'
# password = input("请输入密码:")
# md5_password = hashlib.md5()
# print(md5_password)
# buffer = md5_password
# print(buffer.hexdigest)
# md5_password = hashlib.md5(buffer)
# print(md5_password)
md5 = hashlib.md5()
md5.update(password.encode('gbk'))
print("第一次md5:" + md5.hexdigest())

password = md5.hexdigest()

md5_new = hashlib.md5()
md5_new.update(password.upper().encode('gbk'))
print("第二次md5:" + md5_new.hexdigest())

password = md5_new.hexdigest().upper()
print(password)






# from lxml import html


# session_request = requests.session()
# login_url = "http://192.168.51.90:8080/ump-console/xcom/rbac/logon.do"
# result = session_request.get(login_url)
#
# tree = html.fromstring(result.text)

source = requests.get("http://localhost:8080/ump-console/xcom/rbac/logon.do").text
# print(source)
session = requests.session()

params = {'loginName': 'admin', 'passwordA': 'admin', 'password': password, 'groupId': ''}
# r = requests.post('http://192.168.51.90:8080/ump-console/xcom/rbac/loginAction.do', data=params)
r = session.post('http://localhost:8080/ump-console/xcom/rbac/loginAction.do', data=params)
res = session.get("http://localhost:8080/ump-console/console/report/reportAssetAction.do")
result = res.text
# print(result)
resl = r'method="post" action="(.*?)" id="asdf">'
# resl = r'<iframe src="desktoplr/bot.jsp" name="(.*?)" frameborder="0"'
text = re.findall(resl, result)
print("测试")
print(text)
