# CODING:UTF-8
import json
import unittest

import requests

from interface.xdj_interface_login import InterfaceLogin


class CheckPuTongTest(unittest.TestCase):
    """各地区发票查验接口测试"""
    i = 1

    # 判断是不是第一次查验

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
        try:
            print(self.result)
        except AttributeError as e:
            code = 500
            print('查验失败，服务器报错了,没有返回结果！！！')
            self.assertEqual(code,0)


    # def test_check_invoice_test(self):
    #     """调试普通发票查验成功"""
    #     payload = {'fplx': '04', 'fpdm': '3100172320', 'fphm': '05295992', 'fpje': '', 'jym': '962162',
    #                'kprq': '20171025'}
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     try:
    #         self.result = r.json()
    #         if self.result['code'] != 0 and self.i == 1:
    #             self.i += 1
    #             print("第一次查验失败，进行第 %s 次查验" % (self.i))
    #             self.test_check_invoice_test()
    #         else:
    #             self.assertEqual(self.result['code'], 0)
    #             self.assertEqual(self.result['msg'], '查询成功')
    #     except json.decoder.JSONDecodeError as e:
    #         print(e)
    #         print(r.text)
    #     else:
    #         pass
    #     finally:
    #         pass

    def test_check_invoice_shanghai(self):
        """上海普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '3100162320', 'fphm': '56618159', 'fpje': '', 'jym': '690593',
                   'kprq': '20170213'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_shanghai()
            else:
                self.assertEqual(self.result['code'], 0)
                self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    def test_check_invoice_beijing(self):
        """北京普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '1100171320', 'fphm': '45538707', 'fpje': '', 'jym': '390267',
                   'kprq': '20170915'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_beijing()
            else:
                self.assertEqual(self.result['code'], 0)
                self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    def test_check_invoice_tianjin(self):
        """天津普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '1200172320', 'fphm': '09267390', 'fpje': '', 'jym': '713985',
                   'kprq': '20171023'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_tianjin()
            else:
                self.assertEqual(self.result['code'], 0)
                self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    def test_check_invoice_shenzhen(self):
        """深圳专用发票查验成功"""
        payload = {'fplx': '01', 'fpdm': '4403172130', 'fphm': '04318695', 'fpje': '633.96', 'jym': '',
                   'kprq': '20170813'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_shenzhen()
            else:
                self.assertEqual(self.result['code'], 0)
                self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    def test_check_invoice_hebei(self):
        """河北普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '1300171320', 'fphm': '00271772', 'fpje': '', 'jym': '936815',
                   'kprq': '20170927'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_hebei()
            else:
                self.assertEqual(self.result['code'], 0)
                self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    def test_check_invoice_shanxi(self):
        """山西普通发票查验成功"""
        payload = {'fplx': '01', 'fpdm': '1400171130', 'fphm': '02062714', 'fpje': '17094.03', 'jym': '',
                   'kprq': '20171117'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_shanxi()
            else:
                self.assertEqual(self.result['code'], 0)
                self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass


    def test_check_invoice_neimeng(self):
        """内蒙普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '1500164350', 'fphm': '01058176', 'fpje': '', 'jym': '119257',
                   'kprq': '20170720'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_neimeng()
            else:
                self.assertEqual(self.result['code'], 0)
                self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    def test_check_invoice_liaoning(self):
        """辽宁普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '2100171320', 'fphm': '11695353', 'fpje': '', 'jym': '893273',
                   'kprq': '20170925'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_liaoning()
            else:
                self.assertEqual(self.result['code'], 0)
                self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    def test_check_invoice_jilin(self):
        """吉林普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '2200162350', 'fphm': '01875257', 'fpje': '', 'jym': '878078',
                   'kprq': '20171115'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_jilin()
            else:
                self.assertEqual(self.result['code'], 0)
                self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    def test_check_invoice_zhejiang(self):
        """浙江专用发票查验成功"""
        payload = {'fplx': '01', 'fpdm': '3300154130', 'fphm': '05331852', 'fpje': '53.68', 'jym': '',
                   'kprq': '20171010'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_zhejiang()
            else:
                self.assertEqual(self.result['code'], 0)
                self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    def test_check_invoice_anhui(self):
        """安徽普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '3400172320', 'fphm': '19768327', 'fpje': '', 'jym': '156228',
                   'kprq': '20171020'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_anhui()
            else:
                self.assertEqual(self.result['code'], 0)
                self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    def test_check_invoice_fujian(self):
        """福建普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '3500163350', 'fphm': '21099644', 'fpje': '', 'jym': '920870',
                   'kprq': '20170621'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_fujian()
            else:
                self.assertEqual(self.result['code'], 0)
                self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    def test_check_invoice_jiangxi(self):
        """江西普通发票查验成功"""
        payload = {'fplx': '01', 'fpdm': '3600163130', 'fphm': '06998169', 'fpje': '1522.64', 'jym': '',
                   'kprq': '20171018'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_jiangxi()
            else:
                self.assertEqual(self.result['code'], 0)
                self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    def test_check_invoice_shandong(self):
        """山东普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '3700164320', 'fphm': '33170062', 'fpje': '', 'jym': '690447',
                   'kprq': '20170606'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_shandong()
            else:
                self.assertEqual(self.result['code'], 0)
                self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    def test_check_invoice_henan(self):
        """河南普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '4100171320', 'fphm': '00312101', 'fpje': '', 'jym': '956239',
                   'kprq': '20170606'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_henan()
            else:
                self.assertEqual(self.result['code'], 0)
                self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    def test_check_invoice_hubei(self):
        """湖北普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '4200164320', 'fphm': '47982351', 'fpje': '', 'jym': '464625',
                   'kprq': '20171026'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_hubei()
            else:
                self.assertEqual(self.result['code'], 0)
                self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    def test_check_invoice_hunan(self):
        """湖南普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '4300171320', 'fphm': '04268504', 'fpje': '', 'jym': '288558',
                   'kprq': '20170616'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_hunan()
            else:
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
        payload = {'fplx': '04', 'fpdm': '4400163320', 'fphm': '36198951', 'fpje': '', 'jym': '596043',
                   'kprq': '20170421'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_guangdong()
            else:
                self.assertEqual(self.result['code'], 0)
                self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    def test_check_invoice_guangxi(self):
        """广西普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '4500171320', 'fphm': '15663941', 'fpje': '', 'jym': '249570',
                   'kprq': '20170612'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_guangxi()
            else:
                self.assertEqual(self.result['code'], 0)
                self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    def test_check_invoice_hainan(self):
        """海南普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '4600162320', 'fphm': '09581833', 'fpje': '', 'jym': '264788',
                   'kprq': '20170524'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_hainan()
            else:
                self.assertEqual(self.result['code'], 0)
                self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    def test_check_invoice_shaxi(self):
        """陕西普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '6100171320', 'fphm': '09030275', 'fpje': '', 'jym': '911427',
                   'kprq': '20170626'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_shaxi()
            else:
                self.assertEqual(self.result['code'], 0)
                self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass

    def test_check_invoice_ningxia(self):
        """宁夏普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '6400171320', 'fphm': '02645843', 'fpje': '', 'jym': '932430',
                   'kprq': '20170916'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        try:
            self.result = r.json()
            if self.result['code'] != 0 and self.i == 1:
                self.i += 1
                print("第一次查验失败，进行第 %s 次查验" % self.i)
                self.test_check_invoice_ningxia()
            else:
                self.assertEqual(self.result['code'], 0)
                self.assertEqual(self.result['msg'], '查询成功')
        except json.decoder.JSONDecodeError as e:
            print(e)
            print(r.text)
        else:
            pass
        finally:
            pass


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(CheckPuTongTest("test_check_invoice_shanghai"))
    # rr = CheckPuTongTest()
    # rr.test_check_invoice_test()
