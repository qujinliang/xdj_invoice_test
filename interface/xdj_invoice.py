# CODING:UTF-8
import requests
import unittest
import os, sys
from HTMLTestRunner import HTMLTestRunner
import time
import json
from xdj_interface_login import InterfaceLogin
import csv


class FpxdjInvoiceTest(unittest.TestCase):
    """小当家查验发票接口测试"""

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

    def tearDown(self):
        pass
        print('共查询 %s 张发票' % self.i)

    # print(self.result)


    # def test_zggj(self):





    # def test_check_invoice_zyfp_succe(self):
    # 	'''北京芬芳靓丽商贸有限公司'''
    # 	self.i=0
    # 	with open('fp_data01.csv') as csvfile:
    # 		reader = csv.DictReader(csvfile)
    # 		newo_dict = {}
    # 		for row in reader:
    # 			list1 = ['01',row['fpdm'],row['fphm'],row['kprq'],row['je']]
    # 			list2 = ['fplx','fpdm','fphm','kprq','fpje']
    # 			dicts = dict(zip(list2,list1))
    # 			#print(self.dicts)

    # 		# payload={'fplx':'01', 'fpdm':'1100171130','fphm':'02577178','fpje':"6320.75",
    # 		# 'kprq':'20170816'}
    # 			#print(dicts)
    # 			r = requests.post(self.url, json=dicts, headers=self.headers)
    # 			self.result = r.json()
    # 			try:
    # 				self.assertEqual(self.result['code'],0)
    # 				self.assertEqual(self.result['msg'],'查询成功')
    # 				print(dicts,"查验成功")

    # 			except AssertionError as e:
    # 				print('发票查验失败：',e,dicts)
    # 				raise
    # 			finally:
    # 				self.i += 1

    # def test_check_invoice_losmzyfp_succe(self):
    # 	'''北京朗欧商贸有限公司'''
    # 	self.i=0
    # 	with open('fp_data02.csv') as csvfile:
    # 		reader = csv.DictReader(csvfile)
    # 		newo_dict = {}
    # 		for row in reader:
    # 			list1 = ['01',row['fpdm'],row['fphm'],row['kprq'],row['je']]
    # 			list2 = ['fplx','fpdm','fphm','kprq','fpje']
    # 			dicts = dict(zip(list2,list1))
    # 			#print(self.dicts)

    # 		# payload={'fplx':'01', 'fpdm':'1100171130','fphm':'02577178','fpje':"6320.75",
    # 		# 'kprq':'20170816'}
    # 			#print(dicts)
    # 			r = requests.post(self.url, json=dicts, headers=self.headers)
    # 			self.result = r.json()
    # 			try:
    # 				self.assertEqual(self.result['code'],0)
    # 				self.assertEqual(self.result['msg'],'查询成功')
    # 				print(dicts,"查验成功")

    # 			except AssertionError as e:
    # 				print('发票查验失败：',e,dicts)
    # 				raise
    # 			finally:
    # 				self.i += 1

    # def test_check_invoice_xyhsmzyfp_succe(self):
    # 	'''北京欣雅荟商贸有限公司'''
    # 	self.i=0
    # 	with open('fp_data03.csv') as csvfile:
    # 		reader = csv.DictReader(csvfile)
    # 		newo_dict = {}
    # 		for row in reader:
    # 			list1 = ['01',row['fpdm'],row['fphm'],row['kprq'],row['je']]
    # 			list2 = ['fplx','fpdm','fphm','kprq','fpje']
    # 			dicts = dict(zip(list2,list1))
    # 			#print(self.dicts)

    # 		# payload={'fplx':'01', 'fpdm':'1100171130','fphm':'02577178','fpje':"6320.75",
    # 		# 'kprq':'20170816'}
    # 			#print(dicts)
    # 			r = requests.post(self.url, json=dicts, headers=self.headers)
    # 			self.result = r.json()
    # 			try:
    # 				self.assertEqual(self.result['code'],0)
    # 				self.assertEqual(self.result['msg'],'查询成功')
    # 				print(dicts,"查验成功")

    # 			except AssertionError as e:
    # 				print('发票查验失败：',e,dicts)
    # 				raise
    # 			finally:
    # 				self.i += 1

    def test_check_invoice_bjzxrbzyfp_succe(self):
        '''北京正信悦宝商贸有限公司'''
        self.i = 0
        with open('fp_data04.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            newo_dict = {}
            for row in reader:
                list1 = ['01', row['fpdm'], row['fphm'], row['kprq'], row['je']]
                list2 = ['fplx', 'fpdm', 'fphm', 'kprq', 'fpje']
                dicts = dict(zip(list2, list1))
                # print(self.dicts)

                # payload={'fplx':'01', 'fpdm':'1100171130','fphm':'02577178','fpje':"6320.75",
                # 'kprq':'20170816'}
                # print(dicts)
                r = requests.post(self.url, json=dicts, headers=self.headers)
                self.result = r.json()
                try:

                    self.assertEqual(self.result['code'], 0)
                    self.assertEqual(self.result['msg'], '查询成功')
                    print(dicts, "查验成功")

                except AssertionError as e:
                    print('发票查验失败：', e, dicts)
                    continue

                finally:
                    self.i += 1


if __name__ == '__main__':
    unittest.main()
