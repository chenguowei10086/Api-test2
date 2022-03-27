from hytest import *
from lib.webapi import apimgr

force_tags = ['login_test']
class c1:
    name = '添加客户 - API-0151'




    #清除方法
    def teardown(self):
        apimgr.customer_del(self.addedCustomerId)

    def teststeps(self):

        STEP(1, '添加一个客户')
        r = apimgr.customer_add('武汉市桥西医院',
                            '13345679934',
                            "武汉市桥西医院北路")

        addRet = r.json()

        self.addedCustomerId = addRet['id']

        CHECK_POINT('返回的ret值=0',
                    addRet['ret'] == 0)


        STEP(2, '检查系统数据')

        r = apimgr.customer_list()

        listRet = r.json()

        expected = {
            "ret": 0,
            "retlist": [
                {
                    "address": "武汉市桥西医院北路",
                    "id": addRet['id'],
                    "name": "武汉市桥西医院",
                    "phonenumber": "13345679934"
                }
            ] ,
            'total': 1
        }

        CHECK_POINT('返回的消息体数据正确',
                    expected == listRet)



class c3:
    name = '添加客户 - API-0153'

    def teststeps(self):

        STEP(1, '添加一个客户')
        r = apimgr.customer_add2({
                            "phonenumber":"13345679934",
                            "address":"南京市鼓楼北路"
                        })

        addRet = r.json()


        CHECK_POINT('返回的ret',
                    addRet == {
                        "ret": 1,
                        "msg":  "请求消息参数错误",
                    })


        STEP(2, '检查系统数据')

        r = apimgr.customer_list()

        listRet = r.json()

        CHECK_POINT('返回的消息体数据正确',
                    listRet == {
                    "ret": 0,
                    "retlist": [] ,
                    'total': 0
                })

