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

	self._commit_freq = 1000

	 
