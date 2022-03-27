from hytest import *
from lib.webapi import apimgr

class c4:
    name = '添加客户 - API-0154'

    # 清除方法
    def teardown(self):
        apimgr.customer_del(self.addedCustomerId)

    def teststeps(self):
        STEP(1, '添加一个客户')
        r = apimgr.customer_add('武汉市桥西医院',
                            '13345679934',
                            "武汉市桥西医院北路")

        addRet = r.json()

        CHECK_POINT('返回的ret',
                    addRet['ret'] == 0)

        STEP(2, '检查系统数据')

        r = apimgr.customer_list()

        listRet = r.json()

        self.addedCustomerId = addRet['id']
        expected = {
            "ret": 0,
            "retlist": [
                {
                    "address": "武汉市桥西医院北路",
                    "id": addRet['id'],
                    "name": "武汉市桥西医院",
                    "phonenumber": "13345679934"
                }
            ],
            'total': 1
        }

        CHECK_POINT('返回的消息体数据正确',
                    expected == listRet)
        STEP(3, '修改客户')
        r = apimgr.customer_xg(
                                addRet['id'],
                               "医院",
                               "13345678888",
                                "武汉市桥北医院北路1111111"
        )
        STEP(4, '检查修改数据')

        r = apimgr.customer_list()

        listRet = r.json()

        expected = {
            "ret": 0,
            "retlist": [
                {
                    "id": addRet['id'],
                    "name": "医院",
                    "phonenumber": "13345678888",
                    "address": "武汉市桥北医院北路1111111"
                }
            ],
            'total': 1
        }

        CHECK_POINT('返回的消息体数据正确',
                    expected == listRet)
