import unittest
import requests
import os
from unittestreport import ddt,list_data
from common.handle_conf import conf
from common.handle_excel import HandleExcel
from common.handle_path import DATA_DIR


@ddt
class TestLogin(unittest.TestCase):
    test_data = HandleExcel(os.path.join(DATA_DIR, 'read_excel.xlsx'), 'login').read_excel()

    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    @list_data(test_data)
    def test_login(self, item):
        # 1.准备数据
        base_url = conf.get('env', 'base_url')
        url = base_url + item['url']
        method = item['method']
        headers = eval(conf.get('env', 'headers'))
        param = eval(item['data'])
        expected = eval(item['expected'])

        # 2.发起请求
        response = requests.request(method=method, url=url, json=param, headers=headers)
        res = response.json()
        print(f'当前运行的用例标题为{item["title"]}')
        print('预期结果:', expected)
        print('实际结果:', res)
        # 3.校验结果判断
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
        except AssertionError as e:
            raise e
