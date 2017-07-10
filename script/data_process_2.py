# 2017年7月4日17:08:15
# silei
# 训练模型，查看效果
# 数据文件数一共3183个
# baby，car，food，health，legend，life，love，news，science，sexual
# 129，410，409，406，396，409，158，409，409，38

# -*- coding:UTF-8 -*-

dir = {'baby': 129,'car': 410,'food': 409,'health': 406,'legend': 396,'life': 409,'love': 158,'news': 409,'science': 409,'sexual': 38}
# 设置词典，分别是类别名称和该类别下一共包含的文本数量
data_file_number = 0
# 当前处理文件索引数

def MakeAllWordsList(train_datasseg):
    # 统计词频
	all_words = {}
	for train_dataseg in train_datasseg:
		for word in train_dataseg:
			if word in all_words:  
				all_words[word] += 1
			else:
				all_words[word] = 1
    # 所有出现过的词数目
	# print("all_words length in all the train datas: ", len(all_words.keys()))
    # key函数利用词频进行降序排序
	all_words_reverse = sorted(all_words.items(), key=lambda f:f[1], reverse=True) # 内建函数sorted参数需为list
	for all_word_reverse in all_words_reverse:
		print(all_word_reverse[0], "\t", all_word_reverse[1])
	all_words_list = [all_word_reverse[0] for all_word_reverse in all_words_reverse if len(all_word_reverse[0])>1]
	return all_words_list

if __name__ == "__main__":
	for world_data_name,world_data_number in dir.items():
		while (data_file_number < world_data_number):
			print(world_data_name)
			print(world_data_number)
			print(data_file_number)
			file = open('../data/raw_data/'+world_data_name+'/'+str(data_file_number)+'.txt','r',encoding= 'UTF-8')
			MakeAllWordsList(file)
			for line in file:
				print(line+'\n', end='')
			file.close()