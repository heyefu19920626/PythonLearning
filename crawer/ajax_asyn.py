# -*- coding: utf-8 -*-
import requests
import json


def get_ticket():
    response = requests.get(
        "https://kyfw.12306.cn/otn/leftTicket/queryO?leftTicketDTO.train_date=2018-04-03&leftTicketDTO.from_station"
        "=JNK&leftTicketDTO.to_station=AOH&purpose_codes=ADULT")
    print(response.text)


# 协议:https://
# 域名:kyfw.12306.cn
# 路径:/otn/leftTicket/queryO
# 参数:?leftTicketDTO.train_date=2018-04-03&leftTicketDTO.from_station=JNK&leftTicketDTO.to_station=AOH&purpose_codes=ADULT
# 日期, 始发站, 终点站, 成人票

# get_ticket()

with open("state_name.txt", encoding="utf-8") as file:
    state_info = file.read()
state_name_code = {}
for state_info in state_info.split("@")[1:]:
    state_details = state_info.split("|")
    state_name_code[state_details[2]] = state_details[1]
print(state_name_code)
with open("state_name_code.json", "a", encoding="utf-8") as file:
    json.dump(state_name_code, file, ensure_ascii=False)
print(len(state_name_code))
