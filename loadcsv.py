#CODING:UTF-8
import requests
import unittest
import os,sys,re
import HTMLTestRunner
import time
import json
import xlrd
import time
# 这是一个读取toyoshi.xls.xlsx excel文档中的第2列数据到data数组中
# 然后循环读取data数据中的数据，与url拼接发送get请求，并获取返回的地址信息

# 要访问的url 接口
url = "http://139.217.5.58:5500/check/nssbh/"

# 读取excel文档
wb = xlrd.open_workbook('toyoushi.xls.xlsx')

# 读取excel的第一个工作表
sbd = wb.sheet_by_index(0)

# 读取excel工作表的弟2列
data = sbd.col_values(2)

# data = "110108575219505"

# 定义一个数组
res=[]

# 发送get请求，并获取返回信息的函数
def datashu(url,data=''):
	'''写死的函数， '''
	url = url
	data = data
	#stri = strs
	if data != '':
		for sh in data:
			#print(sh)
			r = requests.post(url+sh)
			#print(r)
	
			try:
				# 返回text格式的结果
				res = r.text
				# res = r.json()
				# 这里应该直接写入到excel
				print(res)
			except Exception as e:
				print(e)
				pass		
			else:
				pass
			finally:
				pass
	else:
		r = requests.post(url+data)
		res = r.text
		print(res)


datashu('http://www.baidu.com/')



