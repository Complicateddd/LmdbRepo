import os
from threading import Thread
from mdb_hander import LMDBHandler

class ThreadFunc(object):
	def __init__(self,func,loopname,**kwargs):
		self.func = func
		self.loopname = loopname
		self.kwargs = kwargs

	def __call__(self):
		self.func(self.loopname,**kwargs)


def muti_thread_session(path_list,data_type,lmdb_savedir):
	thnum = 5 # 线程数
	threads = []
	print('total {} solve with muti-thread at {}'.fromat(len(path_list),thnum))

	Each_num = len(path_list)//thnum
	for thid in range(Each_num):
		data_start = thid*Each_num
		data_end = len(path_list)

		if thid<(thnum-1):
			data_end = (thid-1)*Each_num
		thread = Thread(target = ThreadFunc(base_func,thid,path_list[data_start:data_end],lmdb_savedir,data_type))
		threads.append(thread)

	for i in range(thnum):
		threads[i].start()
		time.sleep(0.001)

	for i in range(thnum):
		threads[i].join()


#### base主体
def base_func(loopname,filelist,lmdb_savedir,data_type):
	lmdb_savepath = '{}/{}-{}'.format(lmdb_savedir,data_type,loopname) # lmdb/train-0 # lmdb/train-1
	hander = LMDBHandler(lmdb_savepath)  # 初始化lmdb
	
	keyname_path = '{}/keyname.txt'.format(lmdb_savepath) ## 外部key
	keyname_list = []

	for idx,file in filelist:
		'''
		核心代码 复写部分
		'''
		image = np.load(file)

		hander.put(file,(image))
		keyname_list.append(file)

	with open(keyname_path,'w') as f:
		for keyname in keyname_list:
			f.write(keyname+'\n')

	hander.close()


if __name__ == '__main__':
	data_base_path = 'home/data/'

	lmdb_savepath = '/home/lmdb'

	if not os.path.exists(lmdb_savepath):
		os.makedirs(lmdb_savepath)

	hold = ['train','val','test']

	for data_type in hold:

		data_type_txt = data_type + '.txt'
		data_list = []
		with open('data_type_txt','r') as f:
			for line in f.readlines():
				data_list.append(data_base_path+line.strip())

		print('Process {}/{}'.format(data_type,len(data_list)))

		muti_thread_session(data_list,data_type,lmdb_savepath)
