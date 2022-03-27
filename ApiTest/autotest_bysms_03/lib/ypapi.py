import requests
from  hytest import *

class YPAPIMgr:

    def _printResponse(self, response):
        INFO('\n\n-------- HTTP response * begin -------')
        INFO(response.status_code)

        for k, v in response.headers.items():
            INFO(f'{k}: {v}')

        INFO('')

        INFO(response.content.decode('utf8'))
        INFO('-------- HTTP response * end -------\n\n')

    def mgr_login(self, username='byhy', password='88888888', useProxy=False):
        self.s = requests.Session()

        if useProxy:
            self.s.proxies.update({'http': 'http://127.0.0.1:8888'})

        response = self.s.post("http://127.0.0.1/api/mgr/signin",
                               data={
                                   'username': username,
                                   'password': password
                               }
                               )

        self._printResponse(response)
        return response
    # 药品操作
    def drug_list(self, pagesize=10, pagenumber=1, keywords=''):
        INFO('列出药品')
        response = self.s.get("http://127.0.0.1/api/mgr/medicines",
                              params={
                                  'action': 'list_medicine',
                                  'pagesize': pagesize,
                                  'pagenum': pagenumber,
                                  'keywords': keywords,
                              })

        self._printResponse(response)
        return response

    def drug_add(self,name,desc,sn):
        INFO('添加药品')
        response = self.s.post("http://127.0.0.1/api/mgr/medicines",
              json={
                    "action":"add_medicine",
                    "data":{
                        "name":name,
                        "desc":desc,
                        "sn":sn
                    }
                })

        self._printResponse(response)
        return response

    def drug_xg(self,cid,name,desc,sn):
        INFO('修改药品')
        response = self.s.post("http://127.0.0.1/api/mgr/medicines",
              json={
                    "action": "modify_medicine",
                    "id": cid,
                  "newdata": {
                    "name":name,
                    "desc":desc,
                    "sn":sn
                  }
                })

        self._printResponse(response)
        return response

    def drug_del(self,cid):
        INFO('删除药品')
        response = self.s.delete("http://127.0.0.1/api/mgr/medicines",
              json={
                    "action":"del_medicine",
                    "id": cid
                })

        self._printResponse(response)
        return response

    def drug_del_all(self):
        response = self.drug_list(100,1)

        theList = response.json()["retlist"]
        for one in theList:
            self.drug_del(one["id"])

ypapimgr = YPAPIMgr()