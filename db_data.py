from pymongo import MongoClient


client = MongoClient('139.217.5.58',27017)
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
fp_list = [{'fphm':'09567190'},{'fphm':'33566746'},{'fphm':'30570755'},{'fphm':'02577178'},
		{'fphm':'02560597'},{'fphm':'00136078'},{'fphm':'02650163'},{'fphm':'56618159'},{'fphm':'22635170'},
		{'fphm':'39398151'}]



#fp_list2 = collection.find({'fphm':'09567190'})

# for i in fp_list2:
# 	if 'gfmc'in i:
# 		print(i.get('gfmc'))
		
	# 删除列表中的发票
	#collection.remove(i)

for i in fp_list:
	collection.remove(i)
	