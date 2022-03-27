from hytest import *
from lib.webapi import apimgr

suite_data_customerids = []

# 初始化方法
def suite_setup():
    global  suite_data_customerids
    INFO('添加10个客户')

    for i in range(10):
        r = apimgr.customer_add(
            f'武汉市桥西医院_{i + 1}',
            f'100000000{i + 1:02d}',
            f"武汉市桥西医院北路_{i + 1}")

        suite_data_customerids.append(r.json()['id'])

def suite_teardown():
    global  suite_data_customerids

    for cid in suite_data_customerids:
        apimgr.customer_del(cid)