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
    i = 1

    def setUp(self):
        # 调用接口登录方法
        self.token = InterfaceLogin()
        self.url = "http://test.fapiaoxx.com/api/v4000/invoice/check"
        self.headers = {
            'Cache-Control': 'no-cache',
            'accessToken': self.token.login(),
            'Origin': 'http://test.fapiaoxx.com',
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
            print("查验失败，服务器报错了,上面的是报错信息 ！！！\n",
                  "=" * 20 + "华丽的分割线" + "=" * 20)
            self.assertEqual(code,0)




    def test_check_invoice_cycg_error(self):
        """所查发票不存在"""
        payload = {'fplx': '10', 'fpdm': '012001700112', 'fphm': '02650183', 'jxlx':'1','fpje': '', 'jym': '782238',
                   'kprq': '20170724'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        self.result = r.json()
        if self.result['code'] == 2:
            # print(self.result)
            self.assertEqual(self.result['code'], 2)
        else:
            # print(self.result)
            try:
                self.assertEqual(self.result['code'], 9)
                self.assertEqual(self.result['result'], '所查发票不存在')
            except KeyError as e:
                self.assertEqual(self.result['code'], 9)
                self.assertEqual(self.result['msg'], '所查发票不存在')

    def test_check_invoice_fplx_error(self):
        """发票类型不存在"""
        payload = {'fplx': '08', 'fpdm': '01200170011', 'fphm': '03374531', 'jxlx':'1','fpje': '', 'jym': '439173',
                   'kprq': '20170724'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        self.result = r.json()
        try:
            self.assertEqual(self.result['code'], 10003)
            self.assertEqual(self.result['msg'],'发票类型：不存在的类型')
        except KeyError as e:
            self.assertEqual(self.result['code'], 10003)
            self.assertEqual(self.result['result'], '发票类型：不存在的类型')

    def test_check_invoice_fpdm_lengt(self):
        """发票代码长度不合法"""
        payload = {'fplx': '04', 'fpdm': '0', 'fphm': '03374531','jxlx':'1', 'fpje': '', 'jym': '439173',
                   'kprq': '20170724'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        self.result = r.json()
        try:
            self.assertEqual(self.result['code'], 10006)
            self.assertEqual(self.result['msg'],'发票代码：不合法的长度')
        except KeyError as e:
            self.assertEqual(self.result['code'], 10006)
            self.assertEqual(self.result['result'], '发票代码：不合法的长度')

    def test_check_invoice_fphm_lengt(self):
        """发票号码长度不合法"""
        payload = {'fplx': '10', 'fpdm': '012001700111', 'fphm': '033','jxlx':'1', 'fpje': '', 'jym': '439173',
                   'kprq': '20170724'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        self.result = r.json()
        try:
            self.assertEqual(self.result['code'], 10009)
            self.assertEqual(self.result['msg'],'发票号码：不合法的长度')
        except KeyError as e:
            self.assertEqual(self.result['code'], 10009)
            self.assertEqual(self.result['result'], '发票号码：不合法的长度')

    def test_check_invoice_jym_lengt(self):
        """发票校验码长度不合法"""
        payload = {'fplx': '04', 'fpdm': '012001700111', 'fphm': '03374531', 'jxlx':'1','fpje': '', 'jym': '43913434',
                   'kprq': '20170724'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        self.result = r.json()
        try:
            self.assertEqual(self.result['code'], 10018)
            self.assertEqual(self.result['msg'],'检验码：不合法的长度')
        except KeyError as e:
            self.assertEqual(self.result['code'], 10018)
            self.assertEqual(self.result['result'], '检验码：不合法的长度')

    def test_check_invoice_kprq_lengt(self):
        """发票日期长度不合法"""
        payload = {'fplx': '04', 'fpdm': '012001700111', 'fphm': '03374531','jxlx':'1', 'fpje': '', 'jym': '439173',
                   'kprq': '20170724343'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        self.result = r.json()
        try:
            self.assertEqual(self.result['code'], 10012)
            self.assertEqual(self.result['msg'],'开票日期：不合法的格式')
        except KeyError as e:
            self.assertEqual(self.result['code'], 10012)
            self.assertEqual(self.result['result'], '开票日期：不合法的格式')

    def test_check_invoice_fpgs_error(self):
        """错误格式的发票"""
        payload = {'fplx': '04', 'fpdm': '1111111111', 'fphm': '11111111', 'jxlx':'1', 'fpje': "", 'jym': '111111',
                   "kprq": "20170810"}
        # print(payload)
        r = requests.post(self.url, json=payload, headers=self.headers)
        self.result = r.json()
        try:
            self.assertEqual(self.result['code'], 105)
            self.assertEqual(self.result['result'], '查询发票不规范')
        except KeyError as e:
            self.assertEqual(self.result['code'], 105)
            self.assertEqual(self.result['msg'], '查询发票不规范')

    def test_check_invoice_fptt_error(self):
        """发票抬头不在查询范围内"""
        payload = {'fplx': '04', 'fpdm': '6500164320', 'fphm': '00774156','jxlx':'1', 'fpje': '', 'jym': '931940',
                   'kprq': '20170418'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        self.result = r.json()
        try:
            self.assertEqual(self.result['code'], 10023)
            self.assertEqual(self.result['result'], '发票抬头不在查询范围内')
        except (KeyError,AssertionError) as e:
            self.assertEqual(self.result['code'], 10023)
            self.assertEqual(self.result['msg'], '发票抬头不在查询范围内')

    def test_check_invoice_fpxx_error(self):
        """无对应发票信息"""
        payload = {'fplx': '10', 'fpdm': '1100171320', 'fphm': '29688656','jxlx':'1', 'fpje': '', 'jym': '079367',
                   'kprq': '20170514'}
        r = requests.post(self.url, json=payload, headers=self.headers)
        self.result = r.json()
        try:
            self.assertEqual(self.result['code'], 6)
            self.assertEqual(self.result['result'], '查验成功发票不一致')
        except KeyError as e:
            self.assertEqual(self.result['code'], 6)
            self.assertEqual(self.result['msg'], '查验成功发票不一致')

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
        payload = {'fplx': '10', 'fpdm': '012001700111', 'fphm': '02650163','jxlx':'1', 'fpje': "", 'jym': '746508',
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

    def test_check_invoice_zyfp_succe(self):
        """专用发票查验成功"""
        payload = {'fplx': '01', 'fpdm': '1100171130', 'fphm': '02577178','jxlx':'1', 'fpje': "6320.75", 'jym': '',
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

    # def test_check_invoice_jsfp_succe(self):
    #     """卷票查验成功"""
    #     payload = {'fplx': '11', 'fpdm': '014001700107', 'fphm': '02560597','jxlx':'1', 'fpje': "", 'jym': '863926',
    #                'kprq': '20170522'}
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

    def test_check_invoice_jdcp_succe(self):
        """机动车销售统一发票查成功"""
        payload = {'fplx': '03', 'fpdm': '161001722600', 'fphm': '00136078','jxlx':'1', 'fpje': '60940.17', 'jym': '',
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

    def test_check_invoice_shanghai(self):
        """上海普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '3100171320', 'fphm': '50621017','jxlx':'1', 'fpje': '', 'jym': '376339',
                   'kprq': '20171104'}
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
        payload = {'fplx': '04', 'fpdm': '1100171320', 'fphm': '45538707', 'jxlx':'1', 'fpje': '', 'jym': '390267',
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
        payload = {'fplx': '04', 'fpdm': '1200172320', 'fphm': '09267390', 'jxlx':'1', 'fpje': '', 'jym': '713985',
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

    def test_check_invoice_hebei(self):
        """河北普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '1300171320', 'fphm': '00271772', 'jxlx':'1', 'fpje': '', 'jym': '936815',
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

    def test_check_invoice_liaoning(self):
        """辽宁普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '2100171320', 'fphm': '11695353', 'jxlx':'1', 'fpje': '', 'jym': '893273',
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

    def test_check_invoice_anhui(self):
        """安徽普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '3400172320', 'fphm': '19768327','jxlx':'1',  'fpje': '', 'jym': '156228',
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

    def test_check_invoice_henan(self):
        """河南普通发票查验成功"""
        payload = {'fplx': '04', 'fpdm': '4100171320', 'fphm': '05326230', 'jxlx':'1', 'fpje': '', 'jym': '710099',
                   'kprq': '20171123'}
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
