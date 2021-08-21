import torch
from torch.utils.data import Dataset
from mdb_hander import LMDBHandler



class LMDB_Dataset_Exp(Dataset):

	def __init__(self,lmdbPath):

		self.lmdb_hander = LMDBHandler(lmdbPath,readonly=True)

		keyname_path = '{}/keyname.txt'.format(lmdbPath)

		self.keyname_list = []

		with open(keyname_path,'r') as f:
			for line in f.readlines():
				self.keyname_list.append(line.strip())


	def __getitem__(self,idx):
		keyname = self.keyname_list[idx]

		data = self.lmdb_hander.get(keyname.encode())

		return data 

	def __len__(self):
		return len(self.keyname_list)

	def close_mdb(self):
		self.lmdb_hander.close()