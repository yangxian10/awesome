class _Engine(object):
	def __init__(self, connect):
		self._connect = connect
	def connect(self):
		return self._connect()

engine = None

class _DbCtx(threading.local):
	"""docstring for _DbCtx"""
	def __init__(self):
		#super _DbCtx, self).__init__()
		self.connection = None
		self.transactions = 0
	def is_init(self):
		return not self.connection is None