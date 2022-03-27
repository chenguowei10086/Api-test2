from hytest import *
from lib.webapi import apimgr

class c2:
    name = '添加客户 - API-0152'

    #清除方法
    def teardown(self):
        apimgr.customer_del(self.addedCustomerId)

    def teststeps(self):

        STEP(1,'先列出客户')
        r = apimgr.customer_list()
        listRet1 = r.json()
        customerlist1 =   listRet1["retlist"]



        STEP(2, '添加一个客户')
        r = apimgr.customer_add('南京市鼓楼医院',
                            '13345679934',
                            "南京市鼓楼北路")

        addRet = r.json()

        self.addedCustomerId = addRet['id']

        CHECK_POINT('返回的ret值=0',
                    addRet['ret'] == 0)


        STEP(3, '再次列出客户')

        r = apimgr.customer_list(11)

        listRet = r.json()

        expected = {
            "ret": 0,
            "retlist": [
                {
                    "address": "南京市鼓楼北路",
                    "id": addRet['id'],
                    "name": "南京市鼓楼医院",
                    "phonenumber": "13345679934"
                }
            ] + customerlist1,
            'total': 11
        }

        CHECK_POINT('返回的消息体数据正确',
                    expected == listRet)

