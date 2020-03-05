import unittest,logging,app
from api.emp_api import EmployeeApi
from utils import assert_common_utils, DBUtils, read_add_emp, read_query_emp, read_modify_emp, read_delete_emp
from parameterized.parameterized import parameterized

# 创建测试类集成unittest.TestCase
class TestEmployee(unittest.TestCase):
    # 初始化unittest函数
    def setUp(self) -> None:
        # 实例化Employee
        self.emp_api = EmployeeApi()

    def tearDown(self) -> None:
        pass

    def test_01_login_success(self):
        # 调用登录
        response = self.emp_api.login("13800000002", "123456")
        # 打印登录结果
        logging.info("员工模块的登录结果为：{}".format(response.json()))

        # 取出令牌。并拼接成Bearer 开头的字符串
        token = "Bearer " + response.json().get("data")
        logging.info("取出的令牌为：{}".format(token))

        # 设置员工模块所需要的请求头
        headers = {"Content-Type": "application/json", "Authorization": token}
        app.HEADERS = headers
        logging.info("员工模块请求头为：{}".format(app.HEADERS))

    @parameterized.expand(read_add_emp)
    def test_02_add_emp(self,username,mobile,http_code,success,code,message):
        # 调用添加员工
        response_add_emp = self.emp_api.add_emp(username, mobile, app.HEADERS)
        logging.info("添加员工接口的结果为：{}".format(response_add_emp.json()))
        # 断言结果：响应状态吗，success，code，message
        assert_common_utils(self, response_add_emp, http_code, success, code, message)

        # 由于添加员工成功后需要保存员工ID给后续的查询修改删除员工使用，所以我们需要保存员工ID
        emp_id = response_add_emp.json().get("data").get("id")
        app.EMPID = emp_id
        logging.info("保存的员工ID为：{}".format(app.EMPID))

    @parameterized.expand(read_query_emp)
    def test_03_query_emp(self,http_code,success,code,message):
        # 调用查询员工
        response_query = self.emp_api.query_emp(app.EMPID,app.HEADERS)
        logging.info("查询员工的结果为：{}".format(response_query.json()))
        # 断言
        assert_common_utils(self,response_query,http_code,success,code,message)

    @parameterized.expand(read_modify_emp)
    def test_04_modify_emp(self,username,http_code,success,code,message):
        # 调用修改员工
        response_modify = self.emp_api.modify_emp(app.EMPID,username,app.HEADERS)
        logging.info("修改员工的结果为：{}".format(response_modify.json()))

        # 调用连接数据库类方法
        with DBUtils() as db:
            # 执行SQL语句
            # 根据添加员工返回的id查询数据库中员工表的username
            sql = "select username from bs_user where id = {};".format(app.EMPID)
            logging.info("要查询的sql语句为：{}".format(sql))
            db.execute(sql)
            # 获取返回结果
            result = db.fetchone()
            logging.info("sql查询的结果为：{}".format(result))
            # 断言
            # 注意：如果是用fetchall()去除数据，那么取出result时需要有两个下标restlt[0][0]
            self.assertEqual(username,result[0])
        # 断言
        assert_common_utils(self,response_modify,http_code,success,code,message)

    @parameterized.expand(read_delete_emp)
    def test_05_delete_emp(self,http_code,success,code,message):
        # 调用删除员工
        response_delete = self.emp_api.delete_emp(app.EMPID,app.HEADERS)
        logging.info("删除员工的结果为：{}".format(response_delete.json()))
        # 断言
        assert_common_utils(self,response_delete,http_code,success,code,message)
