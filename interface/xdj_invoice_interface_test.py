# CODING:UTF-8
import requests
import unittest
import os, sys
import HTMLTestRunner
import time
import json
from interface.xdj_interface_login import InterfaceLogin


class CheckInvoiceTest(unittest.TestCase):
    """小当家发票查验接口测试"""

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
            self.assertEqual(code,0)
            print('查验失败，服务器报错了,没有返回结果！！！')



    def test_check_invoice_cycg_error(self):
        """所查发票不存在"""
        payload = {'fplx': '10', 'fpdm': '012001700112', 'fphm': '02650183', 'fpje': '', 'jym': '782238',
                   'kprq': '20170724'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        self.result = r.json()
        if self.result['code'] == 2:
            # print(self.result)
            self.assertEqual(self.result['code'], 2)
        else:
            # print(self.result)
            self.assertEqual(self.result['code'], 9)
            self.assertEqual(self.result['result'], '所查发票不存在')

    def test_check_invoice_fplx_error(self):
        """发票类型不存在"""
        payload = {'fplx': '08', 'fpdm': '01200170011', 'fphm': '03374531', 'fpje': '', 'jym': '439173',
                   'kprq': '20170724'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], 10003)
        self.assertEqual(self.result['msg'], '发票类型：不存在的类型')

    def test_check_invoice_fpdm_lengt(self):
        """发票代码长度不合法"""
        payload = {'fplx': '04', 'fpdm': '0', 'fphm': '03374531', 'fpje': '', 'jym': '439173',
                   'kprq': '20170724'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], 10006)
        self.assertEqual(self.result['msg'], '发票代码：不合法的长度')

    def test_check_invoice_fphm_lengt(self):
        """发票号码长度不合法"""
        payload = {'fplx': '10', 'fpdm': '012001700111', 'fphm': '033', 'fpje': '', 'jym': '439173',
                   'kprq': '20170724'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], 10009)
        self.assertEqual(self.result['msg'], '发票号码：不合法的长度')

    def test_check_invoice_jym_lengt(self):
        """发票校验码长度不合法"""
        payload = {'fplx': '04', 'fpdm': '012001700111', 'fphm': '03374531', 'fpje': '', 'jym': '43913434',
                   'kprq': '20170724'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], 10018)
        self.assertEqual(self.result['msg'], '检验码：不合法的长度')

    def test_check_invoice_kprq_lengt(self):
        """发票日期长度不合法"""
        payload = {'fplx': '04', 'fpdm': '012001700111', 'fphm': '03374531', 'fpje': '', 'jym': '439173',
                   'kprq': '20170724343'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], 10012)
        self.assertEqual(self.result['msg'], '开票日期：不合法的格式')

    def test_check_invoice_fpgs_error(self):
        """错误格式的发票"""
        payload = {'fplx': '04', 'fpdm': '1111111111', 'fphm': '11111111', 'fpje': "", 'jym': '111111',
                   "kprq": "20170810"}
        # print(payload)
        r = requests.post(self.url, json=payload, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], 105)
        self.assertEqual(self.result['result'], '查询发票不规范')

    def test_check_invoice_fptt_error(self):
        """发票抬头不在查询范围内"""
        payload = {'fplx': '04', 'fpdm': '6500164320', 'fphm': '00774156', 'fpje': '', 'jym': '931940',
                   'kprq': '20170418'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], 10023)
        self.assertEqual(self.result['msg'], '发票抬头不在查询范围内')

    def test_check_invoice_fpxx_error(self):
        """无对应发票信息"""
        payload = {'fplx': '10', 'fpdm': '1100171320', 'fphm': '29688656', 'fpje': '', 'jym': '079367',
                   'kprq': '20170514'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], 6)
        self.assertEqual(self.result['result'], '查询成功发票不一致')

    # def test_check_invoice_total_num(self):
    # 	'''查询次数不足'''
    # 	payload={'fplx':'10','fpdm':'011001600111','fphm':'19183755','fpje':'','jym':'714259',
    # 	'kprq':'20170809'}
    # 	r = requests.post(self.url,json=payload,headers=self.headers)
    # 	self.result = r.json()
    # 	self.assertEqual(self.result['code'],14001)
    # 	self.assertEqual(self.result['msg'],'该企业发票查验张数已超限额，请购买。')

    # def test_check_invoice_miss(self):
    #     """无对应发票信息"""
    #     payload = {'fplx': '04', 'fpdm': '012001700111', 'fphm': '02650163', 'fpje': "", 'jym': '746508',
    #                'kprq': '20170724'}
    #     r = requests.post(self.url, json=payload, headers=self.headers)
    #     self.result = r.json()
    #     self.assertEqual(self.result['code'], 11018)
    #     self.assertEqual(self.result['msg'], '无对应发票信息')

    def test_check_invoice_dzfp_succe(self):
        """电子普通发票查验成功"""
        payload = {'fplx': '10', 'fpdm': '012001700111', 'fphm': '02650163', 'fpje': "", 'jym': '746508',
                   'kprq': '20170724'}
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

    def test_chech_invoice_ptfp_succe(self):
        """普通发票查验成功"""
        self.tt = ''
        payload = {'fplx': '04', 'fpdm': '1100164320', 'fphm': '30570755', 'fpje': "", 'jym': '644263',
                   'kprq': '20170209'}
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

    def test_check_invoice_zyfp_succe(self):
        """专用发票查验成功"""
        payload = {'fplx': '01', 'fpdm': '1100171130', 'fphm': '02577178', 'fpje': "6320.75", 'jym': '',
                   'kprq': '20170816'}
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

    def test_check_invoice_jsfp_succe(self):
        """卷票查验成功"""
        payload = {'fplx': '11', 'fpdm': '014001700107', 'fphm': '02560597', 'fpje': "", 'jym': '863926',
                   'kprq': '20170522'}
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

    def test_check_invoice_jdcp_succe(self):
        """机动车销售统一发票查成功"""
        payload = {'fplx': '03', 'fpdm': '161001722600', 'fphm': '00136078', 'fpje': '60940.17', 'jym': '',
                   'kprq': '20170729'}
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





if __name__ == '__main__':
    unittest.main()
# suite = unittest.TestSuite()
# suite.addTest(CheckInvoiceTest("test_check_invoice_cycg_error"))
# suite.addTest(CheckInvoiceTest("test_check_invoice_fplx_error"))
# suite.addTest(CheckInvoiceTest("test_check_invoice_fpdm_length"))
# suite.addTest(CheckInvoiceTest("test_check_invoice_fphm_length"))
# suite.addTest(CheckInvoiceTest("test_check_invoice_jym_length"))
# suite.addTest(CheckInvoiceTest("test_check_invoice_kprq_length"))
# suite.addTest(CheckInvoiceTest("test_check_invoice_fpgs_error"))
# suite.addTest(CheckInvoiceTest("test_check_invoice_fptt_error"))
# suite.addTest(CheckInvoiceTest("test_check_invoice_fpxx_error"))
# suite.addTest(CheckInvoiceTest("test_check_invoice_total_num"))

# suite.addTest(CheckInvoiceTest("test_check_dianzi_success"))
# suite.addTest(CheckInvoiceTest("test_chech_putong_success"))
# suite.addTest(CheckInvoiceTest("test_check_zhuanpa_sucess"))
# suite.addTest(CheckInvoiceTest("test_check_juanpiao_sucess"))
# suite.addTest(CheckInvoiceTest("test_check_jdcxsfp_sucess"))




# now = time.strftime("%Y-%m-%d %H_%M_%S")
# filename = './report/' + now + '_FPXDJ_Interface_test.html'

# fp = open(filename,'wb')
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='发票小当家接口测试结果',
# 	description= '测试用例：')
# runner.run(suite)
# fp.close()
