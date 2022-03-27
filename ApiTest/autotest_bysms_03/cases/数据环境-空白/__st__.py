from hytest import *
from lib.webapi import apimgr

# 初始化方法
def suite_setup():
    INFO('删除客户、药品、订单')
    apimgr.mgr_login()
    apimgr.order_del_all()
    apimgr.customer_del_all()
    apimgr.medicine_del_all()