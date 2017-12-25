import requests

url = "http://test.fapiaoxx.com/api/v4000/security/login"
user = {"source": "1", "ticket": "", "type": 1, "account": "test@uknower.com", "password": "222222"}
qujinliang = {"source": "1", "ticket": "", "type": 1, "account": "qujinliang@uknower.com", "password": "111111"}

class InterfaceLogin:
    """docstring for ClassName"""

    def __init__(self):
        pass

    def login(self):
        r = requests.post(url, json=user)
        self.result = r.json()
        token = self.result['result']['accessToken']
        return token

    def login2(self):
        r = requests.post(url,json=qujinliang)
        self.result2 = r.json()
        token2 = self.result2['result']['accessToken']
        return token2

    if __name__ == '__main__':
        login()
        login2()

