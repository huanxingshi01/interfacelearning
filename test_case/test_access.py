import pytest
import yaml
from requests import Session
import allure

from businessweixin.api.access import Access
from businessweixin.api.token import Test_token


@allure.feature('通讯录管理')
class TestAccess(Test_token):

    @pytest.fixture(scope='session')
    def token(self, test_get_token):
        return test_get_token

    def setup(self):
        self.access = Access()

    # 插入人员测试用例
    @allure.story('添加人员接口')
    @pytest.mark.parametrize("userid, name, alias, mobile",
                             yaml.safe_load(open('data.yaml', 'r', encoding='utf-8')))
    def test_add(self, userid, name, alias, mobile, token):
        print(token)
        assert self.access.test_insertpp(userid, name, alias, mobile, token)[
                   'errmsg'] == 'created. Warning: wrong json format. '
        assert self.access.test_getpp(userid, token)['userid'] == f'{userid}'
        assert self.access.test_getpp(userid, token)['name'] == f'{name}'
        assert self.access.test_getpp(userid, token)['alias'] == f'{alias}'
        assert self.access.test_getpp(userid, token)['mobile'] == f'{mobile}'

    @allure.story('查询人员接口')
    @pytest.mark.parametrize("userid, token",
                             yaml.safe_load(open('data01.yaml', 'r', encoding='utf-8')))
    def test_get(self, userid, token):
        assert self.access.test_getpp(userid, token)['userid'] == 'zhangsan'
        assert self.access.test_getpp(userid, token)['name'] == '张三'
        assert self.access.test_getpp(userid, token)['alias'] == 'bieming01'

    @allure.story('删除人员接口')
    @pytest.mark.parametrize("userid, token",
                             yaml.safe_load(open('data01.yaml', 'r', encoding='utf-8')))
    def test_delete(self, userid, token):
        assert self.access.test_deletepp(userid, token)
