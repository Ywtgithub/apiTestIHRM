
import requests

# 创建登录的API类
class LoginApi:
    def __init__(self):
        self.login_url = "http://182.92.81.159/api/sys/login"

    def login(self, moible, password):
        jsonData = {"mobile": moible, "password": password}
        return requests.post(self.login_url, json=jsonData)

    def login_params(self,jsData):
        return requests.post(self.login_url,json=jsData)