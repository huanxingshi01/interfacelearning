import requests
import json
import pytest
import yaml

from fankuiyh import Test_Fankui


class Test_Fankui():

    def test_gettoken(self):
        params = {"corpid": "wwd22727bbf345e7d6", "corpsecret": "qB94EY7kqp7kCJCnCKfj6ykUQllSyfxbS_bJMSjL6rw"}
        # print(type(params))
        # params01 = json.loads(params)
        # print(type(params01))
        url = " https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(url=url, params=params)
        token = r.json().get('access_token')
        return token

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

    def test_insertpp(self, userid, name, alias, mobile, department=None):
        token01 = self.test_gettoken()
        if department is None:
            department = [4]
        params = {
            "userid": userid,
            "name": name,
            "alias": alias,
            "mobile": mobile,
            "department": department
        }
        params01 = json.dumps(params, ensure_ascii=False).encode('utf-8')
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token01}"
        r = requests.post(url=url, data=params01)
        return r.json()

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

    def test_getpp(self, userid, token=None):

        if token is None:
            token = self.test_gettoken()
        else:
            token = token

        userid = userid
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}"
        r = requests.post(url=url)
        return r.json()

    def test_delete(self):
        token = self.test_gettoken()
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=zhangsan"
        r = requests.get(url=url)

    @pytest.mark.parametrize("userid, name, alias, mobile",
                             yaml.safe_load(open('data.yaml', 'r', encoding='utf-8')), ids=['正向', '反向', '反向'])
    def test_add(self, userid, name, alias, mobile):
        assert self.test_insertpp(userid, name, alias, mobile)['errmsg'] == 'created. Warning: wrong json format. '
        assert self.test_getpp(userid)['userid'] == f'{userid}'
        assert self.test_getpp(userid)['name'] == f'{name}'
        assert self.test_getpp(userid)['alias'] == f'{alias}'
        assert self.test_getpp(userid)['mobile'] == f'{mobile}'

    @pytest.mark.parametrize("userid, token",
                             yaml.safe_load(open('data01.yaml', 'r', encoding='utf-8')), ids=['反向'])
    def test_get(self, userid, token):
        assert self.test_getpp(userid, token)['userid'] == 'zhangsan'
        assert self.test_getpp(userid, token)['name'] == '张三'
        assert self.test_getpp(userid, token)['alias'] == 'bieming01'



