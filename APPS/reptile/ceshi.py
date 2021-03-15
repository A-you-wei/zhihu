import sys
import os

sys.path.append("../")
from APPS.setting import *
from APPS.config import *
import requests
import json
import calendar
import time
import random
import datetime


class SendData:
    public = Public()
    def response_source_one(self):
        """
        获取知乎用户的唯一标识
        :return:
        """
        self.select = "select * from zhihu_hrefs where biaoshi='6'"
        if sqlFeatures2(self.select):
            num = 0
            for self.data in sqlFeatures2(self.select):
                try:
                    response = requests.get(self.data['hrefs'], headers=self.public.header,
                                            cookies=self.public.cookie).text
                    time.sleep(random.randint(3, 10))
                    data_json = json.loads(response)['data']
                    for data in data_json:
                        author = data['author']['member']
                        url_token = author['url_token']
                        url_id = author['id']
                        select = "select id from tbale_c where name1='" + str(url_token) + "' and users='" + str(
                            self.data['users']) + "'"
                        if sqlFeatures2(select):
                            print('已经存在不需要了')
                            print(calendar.timegm(time.gmtime()))
                        else:
                            print(calendar.timegm(time.gmtime()))
                            insert = "insert into tbale_c(id,name1,user_id,datatimes,biaoshi,users)" \
                                     "values(null,'" + str(url_token) + "','" + str(url_id) + "','" + str(
                                calendar.timegm(time.gmtime())) + "','" + str(self.data['biaoshi']) + "','" + str(
                                self.data['users']) + "')"
                            sqlFeatures2(insert)
                except Exception as e:
                    print(e)
                    num += 1
                    with open('E:\\@知乎老师自己添加问题\\APPS\\every_teacher\\@出现问的url一.txt', 'a+', encoding='utf-8') as fiel:
                        fiel.write(self.data['hrefs'] + '@' + '\n')
                    if num >= 3:
                        print(num)
                        # 这里如果连续出现三就应该从从新获取cookies
        else:
            print('数据库中不存在url')


if __name__ == '__main__':
    send = SendData()
    send.response_source_one()

