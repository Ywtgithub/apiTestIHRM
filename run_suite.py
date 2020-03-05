import unittest
import time
import os
from HTMLTestRunner_PY3 import HTMLTestRunner

suite = unittest.TestLoader().discover("./script",pattern="test*.py")
# report_path = os.path.dirname(os.path.abspath(__file__)) + "/report/ihrm{}.html".format(time.strftime("%Y%m%d %H%M%S"))
report_path = os.path.dirname(os.path.abspath(__file__)) + "/report/ihrm.html"
with open(report_path,mode="wb") as f:
    runner = HTMLTestRunner(f,verbosity=2,title="ihrm系统登录和员工管理模块接口测试报告",description="Chrom80.0+Win10")
    runner.run(suite)