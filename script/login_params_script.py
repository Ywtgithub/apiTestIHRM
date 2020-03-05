import unittest,logging,requests
from api.login import LoginApi
from utils import assert_common_utils, read_login_data
from parameterized.parameterized import parameterized

# 创建登录的测试类，并集成unittest.TestCase
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.login_api = LoginApi()

    def tearDown(self) -> None:
        pass

    # 测试登录
    @parameterized.expand(read_login_data)
    def test_01_login(self,mobile,password,http_code,success,code,message):
        # 调用登录接口
        response = self.login_api.login(mobile,password)
        # 打印结果
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录结果
        assert_common_utils(self,response,http_code,success,code,message)
