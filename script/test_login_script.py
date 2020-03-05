import unittest,logging,requests
from api.login import LoginApi
from utils import assert_common_utils

# 创建登录的测试类，并集成unittest.TestCase
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.login_api = LoginApi()

    def tearDown(self) -> None:
        pass

    # 测试登录成功
    def test_01_login_success(self):
        # 调用登录接口
        response = self.login_api.login("13800000002","123456")
        # 打印结果
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录结果
        assert_common_utils(self,response,200,True,10000,"操作成功")

    # 测试用户名不存在
    def test_02_user_is_not_exist(self):
        # 调用登录接口
        response = self.login_api.login("13900000002", "123456")
        # 打印结果
        logging.info("测试用户名不存在的结果为：{}".format(response.json()))
        # 断言登录结果
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 测试密码错误
    def test_03_password_error(self):
        # 调用登录接口
        response = self.login_api.login("13800000002", "1234567")
        # 打印结果
        logging.info("测试密码错误的结果为：{}".format(response.json()))
        # 断言登录结果
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 测试无参
    def test_04_none_params(self):
        # 无参有点特殊，按照现在的封装无法处理，只能单独处理
        response = requests.post("http://182.92.81.159/api/sys/login")
        # 打印结果
        logging.info("测试无参的结果为：{}".format(response.json()))
        # 断言登录结果
        assert_common_utils(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！")

    # 测试用户名为空
    def test_05_user_is_none(self):
        # 调用登录接口
        response = self.login_api.login("", "1234567")
        # 打印结果
        logging.info("测试用户名为空的结果为：{}".format(response.json()))
        # 断言登录结果
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 测试密码为空
    def test_06_password_is_none(self):
        # 调用登录接口
        response = self.login_api.login("13800000002", "")
        # 打印结果
        logging.info("测试密码为空的结果为：{}".format(response.json()))
        # 断言登录结果
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 少参缺少mobile'
    def test_07_params_lack_mobile(self):
        response = self.login_api.login_params({"password":"123456"})
        # 打印结果
        logging.info("测试少参mobile的结果为：{}".format(response.json()))
        # 断言登录结果
        assert_common_utils(self, response,  200, False, 20001, "用户名或密码错误")

    # 少参缺少password
    def test_08_params_lack_password(self):
        response = self.login_api.login_params({"mobile": "13800000002"})
        # 打印结果
        logging.info("测试少参password的结果为：{}".format(response.json()))
        # 断言登录结果
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 多参 增加一个参数
    def test_09_params_more(self):
        response = self.login_api.login_params({"mobile":"13800000002","password":"123456","aaa":"123456"})
        # 打印结果
        logging.info("测试多参的结果为：{}".format(response.json()))
        # 断言登录结果
        assert_common_utils(self, response, 200,True,10000,"操作成功")

    #  错误参数
    def test_10_params_is_error(self):
        response = self.login_api.login_params({"mobil": "13800000002", "password": "123456"})
        # 打印结果
        logging.info("测试错误参数的结果为：{}".format(response.json()))
        # 断言登录结果
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")