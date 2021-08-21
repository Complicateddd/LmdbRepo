import os
from threading import Thread
from mdb_hander import LMDBHandler
from Muti_thread_session import ThreadFunc,muti_thread_session



def base_func(loopname,filelist,lmdb_savedir,data_type):
	lmdb_savepath = '{}/{}-{}'.format(lmdb_savedir,data_type,loopname) # lmdb/train-0
	hander = LMDBHandler(lmdb_savepath)  # 初始化lmdb
	
	keyname_path = '{}/keyname.txt'.format(lmdb_savepath)
	keyname_list = []

	for idx,file in filelist:
		'''
		核心代码
		'''
		image = np.load(file)

		hander.put(file,(image))
		keyname_list.append(file)

	with open(keyname_path,'w') as f:
		for keyname in keyname_list:
			f.write(keyname+'\n')

	hander.close()


if __name__ == '__main__':
	main()
