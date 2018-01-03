from pymongo import MongoClient
import re

#client = MongoClient('139.219.109.239',27017)  #演示环境
client = MongoClient('40.125.209.24',27017)  #测试环境
db = client.user
db.authenticate("user",'ysyc-mongo-user')
db = client.user
collection = db.fc_invoice_info

#查询发票结合中所有发票
# for i in collection.find():
# 	print(i)

#查询指定fphm的发票
#for i in collection.find({"fphm":"09567190"}):
	#print(i)

# zggj_list = collection.find({'gfmc':'中钢新元矿业发展有限公司','owner':'诸葛亮911'})


# for i in zggj_list:
# 	if 'fphm' in i:
# 		collection.remove(i)

#要删除的发票列表
# fp_list = [{'fphm':'09567190'},{'fphm':'33566746'},{'fphm':'30570755'},{'fphm':'02577178'},
# 		{'fphm':'02560597'},{'fphm':'00136078'},{'fphm':'02650163'},{'fphm':'56618159'},{'fphm':'22635170'},
# 		{'fphm':'39398151'},{'fphm':'29688656'},{'fphm':'00632562'},{'fphm':'45538707'},{'fphm':'09267390'},
# 		{'fphm':'00271772'},{"fphm":'19768327'},{'fphm':'21099644'},{'fphm':'33170062'},{'fphm':'00312101'},
# 		{'fphm':'04268504'},{'fphm':'36198951'},{'fphm':'15663941'},{'fphm':'02645843'}]

fp_list2 = ['09567190','33566746','30570755','02577178','02560597','00136078','02650163','02681209','56618159',
			'22635170','39398151','29688656','00632562','45538707','09267390','00271772','19768327','21099644',
			'33170062','00312101','04268504','36198951','15663941','02645843','09581833','70558475','84196936',
			'12863704','25300518','50894061','06411263','06721529','60245026','23070371','04318695','10808356',
			'03471391','11695353','01058176','09030275']

# fp_list3 = collection.find({'fpdm':re.compile('3100')})
#
# for i in fp_list3:
# 	if i.get('fplx') == '04':
# 		fplx = i.get('fplx')
# 		fpdm = i.get('fpdm')
# 		fphm = i.get('fphm')
# 		fpje = i.get('je')
# 		jym = i.get('jym')
# 		kprq = i.get('kprq')
# 		gfmc = i.get('gfmc')
# 		gfsbh = i.get('gfsbh')
# 		xfmc = i.get('xfmc')
#
# 		print(fplx,fpdm,fphm,fpje,jym,kprq,gfmc,gfsbh,xfmc)
#
# 		print('fpdm %s,fphm %s ' %(fpdm,fphm))
		
	# 删除列表中的发票
	#collection.remove(i)

for i in fp_list2:
	collection.remove({'fphm':i})
