import json
import pytest
from filelock import FileLock

from businessweixin.api.base_api01 import Parents


class Test_token(Parents):
    def test_token01(self):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": "wwd22727bbf345e7d6",
                "corpsecret": "qB94EY7kqp7kCJCnCKfj6ykUQllSyfxbS_bJMSjL6rw"
            }
        }
        res = self.send_api(data)
        print(res['access_token'])
        return res['access_token']

    # def test_gettoken(self):
    #     data = {
    #         'method': 'get',
    #         'url': " https://qyapi.weixin.qq.com/cgi-bin/gettoken",
    #         "params": {
    #             "corpid": "wwd22727bbf345e7d6",
    #             "corpsecret": "qB94EY7kqp7kCJCnCKfj6ykUQllSyfxbS_bJMSjL6rw"}
    #     }
    #     # 那个是case
    #     # print(type(params))
    #     # params01 = json.loads(params)
    #     # print(type(params01))
    #     r = self.send_api(data)
    #     return r['access_token']
    @pytest.fixture(scope='session')
    def test_get_token(self, tmp_path_factory, worker_id):
        if not worker_id:
            # not executing in with multiple workers, just produce the data and let
            # pytest's fixture caching do its job
            return self.test_token01()

        # get the temp directory shared by all workers
        root_tmp_dir = tmp_path_factory.getbasetemp().parent
        # root_tmp_dir=C:\Users\WBPC0154\AppData\Local\Temp\pytest-of-WBPC0154\pytest-19
        print(root_tmp_dir)

        fn = root_tmp_dir / "data.json"
        with FileLock(str(fn) + ".lock"):
            if fn.is_file():
                data = json.loads(fn.read_text())
            else:
                data = self.test_token01()
                fn.write_text(json.dumps(data))
        return data
