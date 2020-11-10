import json
import requests
from businessweixin.api.base_api01 import Parents


class Access(Parents):
    # def test_insertbm(self):
    #     token01 = self.test_gettoken()
    #     params = {
    #         "name": "广州研发中心",
    #         "name_en": "RDGZ",
    #         "parentid": 1,
    #         "order": 1,
    #         "id": 4
    #     }
    #     url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={token01}"
    #     r = requests.post(url=url, json=params)
    # 插入人员
    def test_insertpp(self, userid, name, alias, mobile, token, department=None):
        token = token
        if department is None:
            department = [1]
        params = {
            "userid": userid,
            "name": name,
            "alias": alias,
            "mobile": mobile,
            "department": department
        }
        params01 = json.dumps(params, ensure_ascii=False).encode('utf-8')
        data = {
            "method": 'post',
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}",
            "data": params01
        }
        r = self.send_api(data)
        return r

    # @pytest.mark.parametrize('userid, name', yaml.safe_load(open("data.yaml", 'rb')))
    # def test_insertpperr(self):
    #     token01 = self.test_gettoken()
    #     header = {
    #         "charset": 'utf-8'
    #     }
    #     # params = json.load(open("data01.json", 'r', encoding='utf-8'), ensure_ascii='False')
    #     params = {
    #         "userid": "zhangsan",
    #         "name": "张三",
    #         "alias": "jackzhang",
    #         "mobile": "+86 13800000000",
    #         "department": [4]
    #     }
    #     s1 = json.dumps(params)
    #
    #     # params = json.load(open('data01.json', 'r'))
    #     # params01 = json.dumps(params, ensure_ascii=False).encode('utf-8')
    #     url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token01}"
    #     r = requests.post(url=url, data=s1)
    #     print(r.encoding)
    #     print(r.text)
    # 查询人员
    def test_getpp(self, userid, token):
        token = token
        userid = userid
        data = {
            'method': 'post',
            'url': f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}"
        }
        r = self.send_api(data)
        return r

    # 删除人员
    def test_deletepp(self, userid, token):
        token = token
        data = {
            'method': 'get',
            'url': f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}"
        }
        r = self.send_api(data)
        return r
