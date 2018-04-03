# -*- coding: utf-8 -*-
import requests


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


get_ticket()
