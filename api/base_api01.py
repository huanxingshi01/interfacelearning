import requests


# 这是公共类：封装请求方法
class Parents:
    def send_api(self, req: dict):
        # 请求的封装
        return requests.request(**req).json()
