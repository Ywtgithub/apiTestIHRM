import requests

class EmployeeApi:
    def __init__(self):
        pass

    # 登录
    def login(self, moible, password):
        login_url = "http://182.92.81.159/api/sys/login"
        jsonData = {"mobile": moible, "password": password}
        return requests.post(login_url, json=jsonData)

    # 添加
    def add_emp(self,username,mobile,headers):
        add_url = "http://182.92.81.159/api/sys/user"
        jsData = {"username": username,
                   "mobile": mobile,
                   "timeOfEntry": "2020-02-01",
                    "formOfEmployment": 1,
                     "departmentName": "酱油2部",
                     "departmentId": "1205026005332635648",
                     "correctionTime": "2020-02-03T16:00:00.000Z"}
        return requests.post(add_url,json=jsData,headers=headers)

    # 查询
    def query_emp(self,emp_id,headers):
        query_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id
        return requests.get(query_url, headers=headers)

    # 修改
    def modify_emp(self,emp_id,username,headers):
        modify_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id
        return requests.put(modify_url, json={"username": username}, headers=headers)

    # 删除
    def delete_emp(self,emp_id,headers):
        delete_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id
        return requests.delete(delete_url, headers=headers)