import requests

url = "http://test.fapiaoxx.com/api/v4000/security/login"
user = {"source": "1", "ticket": "", "type": 1, "account": "test@uknower.com", "password": "222222"}
qujinliang = {"source": "1", "ticket": "", "type": 1, "account": "qujinliang@uknower.com", "password": "111111"}

class InterfaceLogin:
    """docstring for ClassName"""

    def __init__(self):
        pass

    def login(self):
        try:
            r = requests.post(url, json=user)
            self.result = r.json()
            token = self.result['result']['accessToken']
            return token
        except KeyError as e:
            print('登录失败！')
            print('错误信息：%s' % e)

    def login2(self):
        try:
            r = requests.post(url, json=user)
            self.result2 = r.json()
            token2 = self.result2['result']['accessToken']
            return token2
        except KeyError as e:
            print('登录失败！')
            print('错误信息: %s' % e)

    if __name__ == '__main__':
        login()
        login2()

