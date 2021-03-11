import sys

sys.path.append('../')  # 新加入的
from APPS.setting import *


def get_select_weibo_first1(sta, end, path,types):
    select = "select name1 from tbale_c where datatimes BETWEEN " + str(sta) + " and " + str(
        end) + " and users='" + str(path) + "' and biaoshi='"+str(types)+"'"
    return MySqlClient(select), sta, end


def get_select_weibo_first3(sta, end,path,types):
    select = "select name1 from tbale_c where datatimes BETWEEN " + str(sta) + " and " + str(end) + " and users='" + str(path) + "' and  biaoshi='"+str(types)+"'"
    return MySqlClient(select), sta, end



