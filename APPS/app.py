from flask import Flask, redirect, request, url_for, g, session, render_template
from APPS.config import *
from dataclasses import dataclass
from APPS.secure import *
import datetime, time
from flask_cors import *

app = Flask(__name__, static_folder="./static", template_folder="./templates")
app.secret_key = "yuxudong123412313123"
app.permanent_session_lifetime = datetime.timedelta(seconds=60 * 60)
CORS(app, supports_credentials=True)


@dataclass
class User:
    id: int
    username: str
    password: str
    types: int


# 1-托福雅思，2-日本
users = [
    # 雅思托福用户
    User(1, "@daiwei@.com", "@daiwei@", 1),
    User(2, "@zhaoyue@.com", "@zhaoyue@", 1),
    User(4, "@hanzhenming@.com", "@hanzhenming@", 1),
    User(5, "@limengran@.com", "@limengran@", 1),
    User(6, "@renshutong@.com", "@renshutong@", 1),
    User(7, "@sunjing@.com", "@sunjing@", 1),
    User(11, "@dingpengda@.com", "@dingpengda@", 1),
    User(12, "@wangfan@.com", "@wangfan@", 1),
    User(13, "@yangzihun@.com", "@yangzihun@", 1),
    # 日本用户
    User(3, "@zhangning@.com", "@zhangning@", 2),
    User(8, "@muhe@.com", "@muhe@", 2),
    User(9, "@wangfang@.com", "@wangfang@", 2),
    User(10, "@liuyanan@.com", "@liuyanan@", 2),

    # ap、sat、act
    User(14, "@yuxudong@.com", "@yuxudong@", 3),

]


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = [u for u in users if u.id == int(session['user_id'])][0]
        g.user = user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 登录操作  现在的session是空的
        session.pop('user_id', None)
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        user = [u for u in users if u.username == username]
        if len(user) > 0:
            user = user[0]
        if user and user.password == password:
            session['user_id'] = user.id
            session['user_type'] = user.types
            return redirect(url_for('project'))
    return render_template('lo_gin.html')


@app.route("/project")
def project():
    if not g.user:
        return redirect(url_for('login'))
    return render_template("project.html")


@app.route("/list_index", methods=['GET', 'POST'])
def list_index():
    if request.method == 'POST':
        id = request.form['id']
        user_id = request.form['user_id']
        ymd = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(
            datetime.datetime.now().day)
        list_user = []
        starts_ends = None
        for i in range(1, 13):
            start = int(time.mktime(time.strptime(str(ymd + ' ' + '08:30:00'), "%Y-%m-%d %H:%M:%S")))

            end = 0
            if i == 1:
                sta = start
                end += sta + i * 3600
            else:
                sta = start + (i - 1) * 3600
                end = start + i * 3600
            contents, s, e = get_select_weibo_first1(sta, end, dictname[user_id], id)
            starts_ends = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(s)) + '至' + time.strftime(
                "%Y-%m-%d %H:%M:%S",
                time.localtime(e))
            datafrom = {
                'data': contents,
                'times': starts_ends
            }
            list_user.append(datafrom)
        import json
        return json.dumps(list_user)


@app.route('/inputID_one', methods=['GET', 'POST'])
def inputs_one():
    """
    请求接口
    :param path:
    :return:
    """
    if request.form['user_id'] in dictname:
        username = dictname[request.form['user_id']]
        type_s = request.form['type']
        if request.method == 'GET':
            return render_template('inputID.html')
        else:
            if 'answer' in request.form['datas']:
                data_content = request.form['datas'].split("/")[-1]
                href = 'https://www.zhihu.com/api/v4/answers/{}/comments?order=reverse&limit=20&offset=0&status=open'.format(
                    data_content)
            else:
                data_content = request.form['datas'].split("/")[-1]
                href = 'https://www.zhihu.com/api/v4/articles/{}/comments?order=reverse&limit=20&offset=0&status=open'.format(
                    data_content)
            id = request.form['id']
            if request.form['datas']:
                select = "select id from zhihu_hrefs where hrefs='" + str(href) + "'"
                if MySqlClient(select) and type_s != str(1):
                    return json.dumps(variable1)
                else:
                    insert = "insert into zhihu_hrefs(id,hrefs,biaoshi,users)" \
                             "values(null,'" + str(href) + "','" + str(id) + "','" + str(username) + "')"
                    MySqlClient(insert)
                    return json.dumps(variable2)
            else:
                return json.dumps(variable3)
    else:
        return json.dumps(variable5)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # 清空session
    session.clear()
    session.pop('user_id', None)
    return render_template('lo_gin.html')


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=BUT)
