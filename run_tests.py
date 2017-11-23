import time,sys
sys.path.append('./interface')
from HTMLTestRunner import HTMLTestRunner
import unittest

#指定测试用例为当前文件夹下的interface目录
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')

if __name__ == '__main__':
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = './report/' + now + 'FPXDJ_Interface_test.html'

	fp = open(filename,'wb')
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='发票小当家接口测试结果',
		description = '测试用例：')
	runner.run(discover)
	fp.close()

	# now = time.strftime("%Y-%m-%d %H_%M_%S")
	# filename = './report/' + now + '_FPXDJ_Interface_test.html'

	# fp = open(filename,'wb')
	# runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='发票小当家接口测试结果',
	# 	description= '测试用例：')
	# runner.run(suite)
	# fp.close()

