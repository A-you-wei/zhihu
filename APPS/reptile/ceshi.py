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


"""
https://www.zhihu.com/api/v4/questions/31026425/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics%3Bdata%5B*%5D.settings.table_of_content.enabled&offset=&limit=3&sort_by=default&platform=desktop
include: data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,attachment,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,is_labeled,paid_info,paid_info_content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_recognized;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics;data[*].settings.table_of_content.enabled
offset: 
limit: 3
sort_by: default
platform: desktop
"""