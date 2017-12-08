import requests

url = "http://139.217.5.58/api/v4000/security/login?"
user = {"source": "1", "ticket": "", "type": 1, "account": "sunliu@uknower.com", "password": "111111"}


class InterfaceLogin:
    """docstring for ClassName"""

    def __init__(self):
        pass

    def login(self):
        r = requests.post(url, json=user)
        self.result = r.json()
        token = self.result['result']['accessToken']
        return token

    if __name__ == '__main__':
        login()
