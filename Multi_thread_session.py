import os
from threading import Thread
import time




class ThreadFunc(object):
	def __init__(self,func,loopname,**kwargs):
		self.func = func
		self.loopname = loopname
		self.kwargs = kwargs

	def __call__(self):
		self.func(self.loopname,**kwargs)


def muti_thread_session(path_list):
	thnum = 5
	threads = []
	print('total {} solve with muti-thread at {}'.fromat(len(path_list),thnum))

	Each_num = len(path_list)//thnum
	for thid in range(Each_num):
		data_start = thid*Each_num
		data_end = len(path_list)

		if thid<(thnum-1):
			data_end = (thid-1)*Each_num
		thread = Thread(target = ThreadFunc(base_func,thid,path_list[data_start:data_end]))
		threads.append(thread)

	for i in range(thnum):
		threads[i].start()
		time.sleep(0.001)

	for i in range(thnum):
		threads[i].join()


def base_func(loopname,filelist):
	'''
	filelist = [path1,path2]
	'''

	for file in filelist:
		'''
		
		核心代码复写
		'''
		image = cv2.read(file)



if __name__ == '__main__':

	fileList = []
	for root,dirs,files in os.walk('home/data'):
		for file in files:
			if file.endwith('.jpg'):
				fileList.append(os.path.join(root,file[:-4]))

	muti_thread_session(fileList)
