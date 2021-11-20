

def performCCA(i, status, nodes):
	power = 0
	NOISE = 0.2
	THRESHOLD = 0.2  # for the time being
	if status == 'start':
		for n in nodes:
			if i == n.getID():
				continue
			else:
				power += n.getTXPower()
		if power+NOISE > THRESHOLD:
#			print (power+NOISE)
			return False
		else:
			return True

	elif status == 'end':
		for key in nodes[i].getCCAResult():
			power += nodes[i].getCCAResult()[key]

		if power+NOISE > THRESHOLD:
#	print power
			return False
		else:
			return True
