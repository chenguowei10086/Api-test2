from hytest import *
from lib.ypapi import ypapimgr

class c6:
    name = '添加药品 - API-0155'




    #清除方法
    def teardown(self):
        ypapimgr.drug_del(self.addedCustomerId)

    def teststeps(self):

        STEP(1, '添加一个药品')
        ypapimgr.mgr_login()
        r = ypapimgr.drug_add('青霉素',
                            '青霉素',
                            "234324234234")

        addRet = r.json()

        self.addedCustomerId = addRet['id']

        CHECK_POINT('返回的ret值=0',
                    addRet['ret'] == 0)


        STEP(2, '检查系统数据')

        r = ypapimgr.drug_list()

        listRet = r.json()

        expected = {
            "ret": 0,
            "retlist": [
                {
                    "name": "青霉素",
                    "id": addRet['id'],
                    "desc": "青霉素",
                    "sn": "234324234234"
                }
            ] ,
            'total': 1
        }

        CHECK_POINT('返回的消息体数据正确',
                    expected == listRet)