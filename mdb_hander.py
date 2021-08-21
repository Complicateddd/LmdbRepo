import time
import lmdb
import pyarrow as pa



KB=1024
MB=KB*1024
GB=MB*1024
TB=GB*1024



class LMDBHandler(object):
	def __init__(self, 
		path = None, 
		map_size = 0.5*TB,
		readonly = False,
		metasync = True):

	self.db = lmdb.open(path,map_size=map_size,readonly=readonly,metasync=metasync)

	self.wtx = self.db.begin(write=True) if not readonly else None

	self.rtx = self.db.begin(write=False)

	self.commit_freq = 1000

	self.len = self.get_length()

	def put(self, key:str, value):

		self.len += 1
		self.wtx.put(key.encode(),pa.serialize(value).to_buffer())

		if self.len % self.commit_freq ==0:
			self.wtx.commit()
			self.wtx = self.db.begin(write=True)

	def get(self,key):
		buff = self.rtx.get(key)
		return pa.deserialize(buff) if buff else buff

	def delete(self,key):
		self.wtx.delete(key)
		self.wtx.commit()
		self.wtx = self.db.begin(write=True)

	def get_keys(self):
		keys = []
		with self.db.begin(write=False) as txt: 
			for key,val in txt.cursor():
				keys.append(key)
		return keys

	def get_length(self):
		with self.db.begin(write=False) as txt:
			retrn txt.stat()['entries']

	def close(self):

		if self.wtx != None:
			self.wtx.commit()

		if self.rtx != None:
			self.rtx.commit()

		if self.wtx != None:
			self.db.sync()

		self.db.close()

	def __enter__(self):
		return self

	def __exit__(self,exc_type,exc_val,exc_tb):
		self.close()

if __name__ == '__main__':
 	pass 