from Node import Node

class event(object):
	def __init__(self,argv):
		self.time = argv['time']
		self.actType = argv['actType']
		self.src = argv['src']
		self.des = argv['des']
		self.pacSize = argv['pacSize']
		self.pacData = argv['pacData']
		self.pacType = argv['pacType']
		self.pacAckReq = argv['pacAckReq']


