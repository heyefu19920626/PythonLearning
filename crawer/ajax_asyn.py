# -*- coding: utf-8 -*-
import requests
import json


def get_ticket(from_station, to_station):
    response = requests.get(
        "https://kyfw.12306.cn/otn/leftTicket/queryO?leftTicketDTO.train_date=2018-04-03&leftTicketDTO.from_station"
        "=" + from_station + "&leftTicketDTO.to_station=" + to_station + "&purpose_codes=ADULT")
    print(response.text)


# 协议:https://
# 域名:kyfw.12306.cn
# 路径:/otn/leftTicket/queryO
# 参数:?leftTicketDTO.train_date=2018-04-03&leftTicketDTO.from_station=JNK&leftTicketDTO.to_station=AOH&purpose_codes=ADULT
# 日期, 始发站, 终点站, 成人票

with open("state_name.txt", encoding="utf-8") as file:
    state_info = file.read()
state_dict = {}
for state_info in state_info.split("@")[1:]:
    state_details = state_info.split("|")
    state_dict[state_details[1]] = state_details[2]
with open("state_name_code.json", "a", encoding="utf-8") as file:
    json.dump(state_dict, file, ensure_ascii=False)

get_ticket(state_dict['成都'], state_dict['上海'])
