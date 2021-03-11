# coding=utf-8
# 连接mysql接口
import requests, json
import pymysql


def MySqlClient(sql_statement=None):
    """
       :查询的增删改查
       :param sql_statement:
       :return:
       yuxudong
       """
    conn = pymysql.connect(host='192.168.60.78', user='root', password='131556', port=3306, db='zhihu', charset='utf8')
    cursor = conn.cursor()
    if 'insert' in sql_statement:
        sql = sql_statement
        cursor.execute(sql)
        conn.commit()
    elif 'select' in sql_statement:
        sql = sql_statement
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql)
        return cur.fetchall()
    elif 'update' in sql_statement:
        sql = sql_statement
        cursor.execute(sql)
        conn.commit()
    elif 'show' in sql_statement:
        sql = sql_statement
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql)
        return cur.fetchall()




def sqlFeatures1(sql_statement=None):
    conn = pymysql.connect(host='192.168.60.78', user='root', password='131556', db='weibo', port=3306)
    cursor = conn.cursor()
    """
    :查询的增删改查
    :param sql_statement:
    :return:
    """
    if 'insert' in sql_statement:
        sql = sql_statement
        cursor.execute(sql)
        conn.commit()
    elif 'select' in sql_statement:
        sql = sql_statement
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql)
        return cur.fetchall()
    elif 'update' in sql_statement:
        sql = sql_statement
        cursor.execute(sql)
        conn.commit()
    elif 'show' in sql_statement:
        sql = sql_statement
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql)
        return cur.fetchall()

def sqlFeatures2(sql_statement=None):
    conn = pymysql.connect(host='192.168.60.78', user='root', password='131556', db='zhihu', port=3306)
    cursor = conn.cursor()
    """
    :查询的增删改查
    :param sql_statement:
    :return:
    """
    if 'insert' in sql_statement:
        sql = sql_statement
        cursor.execute(sql)
        conn.commit()
    elif 'select' in sql_statement:
        sql = sql_statement
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql)
        return cur.fetchall()
    elif 'update' in sql_statement:
        sql = sql_statement
        cursor.execute(sql)
        conn.commit()
    elif 'show' in sql_statement:
        sql = sql_statement
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql)
        return cur.fetchall()



class Public:
    def __init__(self):
        """
        初始化变量
        :param data:
        :return:
        """

        self.url = "https://www.zhihu.com/api/v4/messages"
        self.select = "select * from cookies"
        self.c = sqlFeatures2(self.select)
        self.cookie = self.c[0]

        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
        }


    def responses(self):
        res = requests.post(url=self.url, headers=self.header,cookies=self.cookie).text
        return res



