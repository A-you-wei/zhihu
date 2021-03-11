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

    def Send(self, datafrom):
        """
        发送请求
        :param data:
        :return:
        """
        data = {'type': 'common', 'receiver_hash': str(datafrom), 'content': '哈喽   看到你有找雅思老师~'}
        self.html = requests.post(self.public.url, json=data, cookies=self.public.cookie, headers=self.public.header)
        print(self.html.status_code)
        print(self.html.text)
        update = "update tbale_one set biaoshi='1' where user_id='" + str(datafrom) + "'"
        sqlFeatures2(update)

    def response_source_one(self):
        """
        获取知乎用户的唯一标识
        :return:
        """
        self.select = "select * from zhihu_hrefs where biaoshi='4'"
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

    def response_source_two(self):
        select = "select * from tbale_one where biaoshi is null"
        list_user_id = []
        for data_every in sqlFeatures2(select):
            user_id = data_every['user_id']
            list_user_id.append(user_id)
        return list_user_id


if __name__ == '__main__':

    while True:
        ymd = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(
            datetime.datetime.now().day)
        hms = str(datetime.datetime.now().hour) + ':' + str(datetime.datetime.now().minute) + ':' + str(
            datetime.datetime.now().second)
        requests.adapters.DEFAULT_RETRIES = 5
        s = requests.session()
        s.keep_alive = False
        if int(time.mktime(time.strptime(str(ymd + ' ' + hms), "%Y-%m-%d %H:%M:%S"))) == int(
                time.mktime(time.strptime(str(ymd + ' ' + '10:00:00'), "%Y-%m-%d %H:%M:%S"))):
            send = SendData()
            send.response_source_one()
        elif int(time.mktime(time.strptime(str(ymd + ' ' + hms), "%Y-%m-%d %H:%M:%S"))) == int(
                time.mktime(time.strptime(str(ymd + ' ' + '09:00:00'), "%Y-%m-%d %H:%M:%S"))):
            send = SendData()
            send.response_source_one()
        elif int(time.mktime(time.strptime(str(ymd + ' ' + hms), "%Y-%m-%d %H:%M:%S"))) == int(
                time.mktime(time.strptime(str(ymd + ' ' + '09:30:00'), "%Y-%m-%d %H:%M:%S"))):
            send = SendData()
            send.response_source_one()
        elif int(time.mktime(time.strptime(str(ymd + ' ' + hms), "%Y-%m-%d %H:%M:%S"))) == int(
                time.mktime(time.strptime(str(ymd + ' ' + '10:30:00'), "%Y-%m-%d %H:%M:%S"))):
            send = SendData()
            send.response_source_one()
        elif int(time.mktime(time.strptime(str(ymd + ' ' + hms), "%Y-%m-%d %H:%M:%S"))) == int(
                time.mktime(time.strptime(str(ymd + ' ' + '11:30:00'), "%Y-%m-%d %H:%M:%S"))):
            send = SendData()
            send.response_source_one()
        elif int(time.mktime(time.strptime(str(ymd + ' ' + hms), "%Y-%m-%d %H:%M:%S"))) == int(
                time.mktime(time.strptime(str(ymd + ' ' + '13:30:00'), "%Y-%m-%d %H:%M:%S"))):
            send = SendData()
            send.response_source_one()
        elif int(time.mktime(time.strptime(str(ymd + ' ' + hms), "%Y-%m-%d %H:%M:%S"))) == int(
                time.mktime(time.strptime(str(ymd + ' ' + '14:30:00'), "%Y-%m-%d %H:%M:%S"))):
            send = SendData()
            send.response_source_one()
        elif int(time.mktime(time.strptime(str(ymd + ' ' + hms), "%Y-%m-%d %H:%M:%S"))) == int(
                time.mktime(time.strptime(str(ymd + ' ' + '15:30:00'), "%Y-%m-%d %H:%M:%S"))):
            send = SendData()
            send.response_source_one()
        elif int(time.mktime(time.strptime(str(ymd + ' ' + hms), "%Y-%m-%d %H:%M:%S"))) == int(
                time.mktime(time.strptime(str(ymd + ' ' + '16:30:00'), "%Y-%m-%d %H:%M:%S"))):
            send = SendData()
            send.response_source_one()
        elif int(time.mktime(time.strptime(str(ymd + ' ' + hms), "%Y-%m-%d %H:%M:%S"))) == int(
                time.mktime(time.strptime(str(ymd + ' ' + '17:30:00'), "%Y-%m-%d %H:%M:%S"))):
            send = SendData()
            send.response_source_one()
        elif int(time.mktime(time.strptime(str(ymd + ' ' + hms), "%Y-%m-%d %H:%M:%S"))) == int(
                time.mktime(time.strptime(str(ymd + ' ' + '18:30:00'), "%Y-%m-%d %H:%M:%S"))):
            send = SendData()
            send.response_source_one()
        elif int(time.mktime(time.strptime(str(ymd + ' ' + hms), "%Y-%m-%d %H:%M:%S"))) == int(
                time.mktime(time.strptime(str(ymd + ' ' + '19:30:00'), "%Y-%m-%d %H:%M:%S"))):
            send = SendData()
            send.response_source_one()
        elif int(time.mktime(time.strptime(str(ymd + ' ' + hms), "%Y-%m-%d %H:%M:%S"))) == int(
                time.mktime(time.strptime(str(ymd + ' ' + '20:30:00'), "%Y-%m-%d %H:%M:%S"))):
            send = SendData()
            send.response_source_one()
        else:
            time.sleep(1)
            print('不是获取的时间，请等待... ...')

