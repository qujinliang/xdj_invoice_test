#CODING:UTF-8
import requests
import unittest
import os,sys
import HTMLTestRunner
import time
import json
import csv

# with open('fp_data01.csv') as csvfile:
# 	reader = csv.DictReader(csvfile)
# 	newo_dict = {}
# 	for row in reader:
# 		list1 = [row['fplx'],row['fpdm'],row['fphm'],row['kprq'],row['je']]
# 		list2 = ['fplx','fpdm','fphm','kprq','je']
# 		dicts = dict(zip(list2,list1))
# 		print(dicts)
# 		return (dicts)
	
		





# url = "http://139.217.5.58/api/v4000/invoice/check"
# login_url = "http://139.217.5.58/api/v4000/security/login?"
# user = {"source":"1","ticket":"", "type":0,"account":"13718369579","password":"123456"}
# headers = { 'content-type': "application/json",
#     		'cache-control': "no-cache",}

# r = requests.post(login_url,json=user)

# def test_check_invoice_zyfp_succe():
# 	'''专用发票查验成功'''
# 	payload={}
# 	with open('fp_data01.csv') as csvfile:
# 		reader = csv.DictReader(csvfile)
# 		newo_dict = {}
# 		for row in reader:
# 			list1 = [row['fplx'],row['fpdm'],row['fphm'],row['kprq'],row['je']]
# 			list2 = ['fplx','fpdm','fphm','kprq','je']
# 			dicts = dict(zip(list2,list1))
# 			#print(dicts)

# 	# payload={'fplx':'01', 'fpdm':'1100171130','fphm':'02577178','fpje':"6320.75",
# 	# 'kprq':'20170816'}
# 			r = requests.post(self.url, json=dicts, headers=self.headers)
# 			self.result = r.json()
# 			self.assertEqual(self.result['code'],0)
# 			self.assertEqual(self.result['msg'],'查询成功')
i=0
i +=1
print('义工 %s 张' %i)

a = 123
if type(a) is True:
	print(1)

# res = r.json()
# token = res['result']['accessToken']
# #token = r.cookies.items()[0][1]
# cookies = r.cookies

# print(res)
# #print(type(token))
# print(token)
# print(cookies)
# print(r.headers)
# print(r.url)




# payload = "{\n    \"fplx\": \"04\",\n    \"fpdm\": \"1111111111\",\n    \"fphm\": \"11111111\",\n    \"fpje\": \"\",\n    \"jym\": \"111111\",\n    \"kprq\": \"20170912\"\n}"
# headers = {
#     'content-type': "application/json",
#     'accessToken' : token ,
#     'cache-control': "no-cache",
#     'postman-token': "5f96259d-a380-bbb0-d818-7a2f1f952227"
#     }

# response = requests.request("POST", url, data=payload, headers=headers)

# print(response.json())

