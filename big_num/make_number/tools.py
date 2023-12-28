#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# author@zhaopeng
# @time: 2023/12/27 16:54

import requests


class GetMetaDataInfo():

    def get_pre_event(self):
        path = "/api/backend/track-event/search"
        params = {"offset": "90", "limint": "10", "keyword": "$"}
        headers = {"X-Product-Unique-Id": "DC", "X-Project-Id": "46",
                   "Authorization": "Bearer ce71581a-0bdf-47dc-a825-b23a1ef30117"}
        response = requests.request("GET", "http://uat-uba.growingio.cn/api/backend/track-event/search", params=params,
                                    headers=headers)
        print(response.json())


if __name__ == '__main__':
    a = GetMetaDataInfo()
    a.get_pre_event()
