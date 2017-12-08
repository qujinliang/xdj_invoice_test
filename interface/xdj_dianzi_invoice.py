# CODING:UTF-8
import json
import unittest

import requests

from interface.xdj_interface_login import InterfaceLogin


class CheckPuTongTest(unittest.TestCase):
    """电子发票查验接口测试"""

    def setUp(self):
        # 调用接口登录方法
        self.token = InterfaceLogin()
        self.url = "http://139.217.5.58/api/v4000/invoice/check"
        self.headers = {
            'Cache-Control': 'no-cache',
            'accessToken': self.token.login(),
            'Origin': 'http://139.217.5.58',
            'Content-Type': 'application/json',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8'
        }

    # print(self.headers)

    def tearDown(self):
        # pass
        if self.result is not None:
            print(self.result)
        else:
            pass

    def test_check_invoice_shanghai(self):
        """上海电子发票查验成功"""
        payload = {'fplx': '10', 'fpdm': '031001600411', 'fphm': '70558475', 'fpje': '', 'jym': '027893',
                   'kprq': '20170624'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            self.assertEqual(self.result['code'], 0)
            self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    # def test_check_invoice_beijing(self):
    #     """北京电子发票查验成功"""
    #     payload = {'fplx': '10', 'fpdm': '011001600111', 'fphm': '10808356', 'fpje': '', 'jym': '955183',
    #                'kprq': '20170724'}
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         self.assertEqual(self.result['code'], 0)
    #         self.assertEqual(self.result['msg'], '查询成功')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #     else:
    #         pass
    #     finally:
    #         pass

    def test_check_invoice_tianjin(self):
        """天津电子发票查验成功"""
        payload = {'fplx': '10', 'fpdm': '012001600111', 'fphm': '84196936', 'fpje': '', 'jym': '904686',
                   'kprq': '20170719'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            self.assertEqual(self.result['code'], 0)
            self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    # def test_check_invoice_hebei(self):
    #     """河北电子发票查验成功"""
    #     payload = {'fplx': '10', 'fpdm': '1300171320', 'fphm': '00271772', 'fpje': '', 'jym': '936815',
    #                'kprq': '20170927'}
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         self.assertEqual(self.result['code'], 0)
    #         self.assertEqual(self.result['msg'], '查询成功')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #     else:
    #         pass
    #     finally:
    #         pass

    # def test_check_invoice_shanxi(self):
    #     """山西电子发票查验成功"""
    #     payload = {'fplx': '10', 'fpdm': '014001600111', 'fphm': '12863704', 'fpje': '', 'jym': '489819',
    #                'kprq': '20170701'}
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         self.assertEqual(self.result['code'], 0)
    #         self.assertEqual(self.result['msg'], '查询成功')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #     else:
    #         pass
    #     finally:
    #         pass

    def test_check_invoice_neimeng(self):
        """内蒙电子发票查验成功"""
        payload = {'fplx': '10', 'fpdm': '015001700111', 'fphm': '25300518', 'fpje': '', 'jym': '544484',
                   'kprq': '20171017'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            self.assertEqual(self.result['code'], 0)
            self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    # def test_check_invoice_liaoning(self):
    #     """辽宁普通发票查验成功"""
    #     payload = {'fplx': '10', 'fpdm': '2100171320', 'fphm': '11695353', 'fpje': '', 'jym': '893273',
    #                'kprq': '20170925'}
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         self.assertEqual(self.result['code'], 0)
    #         self.assertEqual(self.result['msg'], '查询成功')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #     else:
    #         pass
    #     finally:
    #         pass

    # def test_check_invoice_jilin(self):
    #     """吉林普通发票查验成功"""
    #     payload = {'fplx': '10', 'fpdm': '2300171320', 'fphm': '11695353', 'fpje': '', 'jym': '893273',
    #                'kprq': '20170925'}
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         self.assertEqual(self.result['code'], 0)
    #         self.assertEqual(self.result['msg'], '查询成功')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #     else:
    #         pass
    #     finally:
    #         pass

    # def test_check_invoice_zhejiang(self):
    #     """江苏电子发票查验成功"""
    #     payload = {'fplx': '10', 'fpdm': '3200171320', 'fphm': '11695353', 'fpje': '', 'jym': '893273',
    #                'kprq': '20170925'}
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         self.assertEqual(self.result['code'], 0)
    #         self.assertEqual(self.result['msg'], '查询成功')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #     else:
    #         pass
    #     finally:
    #         pass


    def test_check_invoice_zhejiang(self):
        """浙江电子发票查验成功"""
        payload = {'fplx': '10', 'fpdm': '033001600211', 'fphm': '50894061', 'fpje': '', 'jym': '895954',
                   'kprq': '20170424'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            self.assertEqual(self.result['code'], 0)
            self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    # def test_check_invoice_anhui(self):
    #     """安徽电子发票查验成功"""
    #     payload = {'fplx': '04', 'fpdm': '3400172320', 'fphm': '19768327', 'fpje': '', 'jym': '156228',
    #                'kprq': '20171020'}
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         self.assertEqual(self.result['code'], 0)
    #         self.assertEqual(self.result['msg'], '查询成功')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #     else:
    #         pass
    #     finally:
    #         pass

    # def test_check_invoice_fujian(self):
    #     """福建电子发票查验成功"""
    #     payload = {'fplx': '04', 'fpdm': '3500163350', 'fphm': '21099644', 'fpje': '', 'jym': '920870',
    #                'kprq': '20170621'}
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         self.assertEqual(self.result['code'], 0)
    #         self.assertEqual(self.result['msg'], '查询成功')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #     else:
    #         pass
    #     finally:
    #         pass

    # def test_check_invoice_jiangxi(self):
    #     """江西普通发票查验成功"""
    #     payload = {'fplx': '04', 'fpdm': '3600163350', 'fphm': '21099644', 'fpje': '', 'jym': '920870',
    #                'kprq': '20170621'}
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         self.assertEqual(self.result['code'], 0)
    #         self.assertEqual(self.result['msg'], '查询成功')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #     else:
    #         pass
    #     finally:
    #         pass

    def test_check_invoice_shandong(self):
        """山东普通发票查验成功"""
        payload = {'fplx': '10', 'fpdm': '037001600111', 'fphm': '06411263', 'fpje': '', 'jym': '701888',
                   'kprq': '20170402'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            self.assertEqual(self.result['code'], 0)
            self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    # def test_check_invoice_henan(self):
    #     """河南普通发票查验成功"""
    #     payload = {'fplx': '04', 'fpdm': '4100171320', 'fphm': '00312101', 'fpje': '', 'jym': '956239',
    #                'kprq': '20170606'}
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         self.assertEqual(self.result['code'], 0)
    #         self.assertEqual(self.result['msg'], '查询成功')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #     else:
    #         pass
    #     finally:
    #         pass

    # def test_check_invoice_hubei(self):
    #     """湖北普通发票查验成功"""
    #     payload = {'fplx': '04', 'fpdm': '4200171320', 'fphm': '00312101', 'fpje': '', 'jym': '956239',
    #                'kprq': '20170606'}
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         self.assertEqual(self.result['code'], 0)
    #         self.assertEqual(self.result['msg'], '查询成功')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #     else:
    #         pass
    #     finally:
    #         pass

    def test_check_invoice_hunan(self):
        """湖北普通发票查验成功"""
        payload = {'fplx': '10', 'fpdm': '043001600111', 'fphm': '06721529', 'fpje': '', 'jym': '896824',
                   'kprq': '20170320'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            self.assertEqual(self.result['code'], 0)
            self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    def test_check_invoice_guangdong(self):
        """广东普通发票查验成功"""
        payload = {'fplx': '10', 'fpdm': '044001600211', 'fphm': '60245026', 'fpje': '', 'jym': '674227',
                   'kprq': '20170203'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            self.assertEqual(self.result['code'], 0)
            self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    # def test_check_invoice_guangxi(self):
    #     """广西普通发票查验成功"""
    #     payload = {'fplx': '04', 'fpdm': '4500171320', 'fphm': '15663941', 'fpje': '', 'jym': '249570',
    #                'kprq': '20170612'}
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         self.assertEqual(self.result['code'], 0)
    #         self.assertEqual(self.result['msg'], '查询成功')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #     else:
    #         pass
    #     finally:
    #         pass

    # def test_check_invoice_hainan(self):
    #     """海南普通发票查验成功"""
    #     payload = {'fplx': '04', 'fpdm': '4600162320', 'fphm': '09581833', 'fpje': '', 'jym': '264788',
    #                'kprq': '20170524'}
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         self.assertEqual(self.result['code'], 0)
    #         self.assertEqual(self.result['msg'], '查询成功')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #     else:
    #         pass
    #     finally:
    #         pass

    def test_check_invoice_shaxi(self):
        """陕西普通发票查验成功"""
        payload = {'fplx': '10', 'fpdm': '061001605111', 'fphm': '23070371', 'fpje': '', 'jym': '703425',
                   'kprq': '20170605'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            self.assertEqual(self.result['code'], 0)
            self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    # def test_check_invoice_ningxia(self):
    #     """宁夏普通发票查验成功"""
    #     payload = {'fplx': '04', 'fpdm': '6400171320', 'fphm': '02645843', 'fpje': '', 'jym': '932430',
    #                'kprq': '20170916'}
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         self.assertEqual(self.result['code'], 0)
    #         self.assertEqual(self.result['msg'], '查询成功')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #     else:
    #         pass
    #     finally:
    #         pass




if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(CheckPuTongTest("test_check_invoice_shanghai"))

