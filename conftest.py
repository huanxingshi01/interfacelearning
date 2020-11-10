import json
from filelock import FileLock
import pytest
from businessweixin.api.base_api01 import Parents


def pytest_collection_modifyitems(items: list) -> None:
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")

