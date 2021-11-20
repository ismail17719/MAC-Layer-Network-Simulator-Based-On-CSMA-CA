from Node import Node
from event import event
import globals as stats

def init(t, src, n):
	argv = {}
	argv['time'] = t
	argv['actType'] = 'sendMac'
	argv['src'] = src
	argv['des'] = n - 1
	argv['pacSize'] = stats.PACKET_SIZE
	argv['pacData'] = src
	argv['pacType'] = 'data'
	argv['pacAckReq'] = True
	e = event(argv)
	return e

