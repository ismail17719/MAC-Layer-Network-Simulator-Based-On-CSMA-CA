from Node import Node
import globals as stats
from perform import act
import operator
import random
from init import init
import csv
import numpy as np
import os
import time
import csv

def simulate(number):
	numOfNodes = number+1

	nodes = []

	for i in range(numOfNodes):  # initialize nodes
		argv = {}
		argv['ID'] = i
		argv['src'] = i
		argv['des'] = numOfNodes - 1
		n = Node(argv)
		nodes.append(n)

	eventList = []
	#for i in range(numOfNodes-1):
	#	nodes[i].setPacInterval(dataRate)

	for i in range(numOfNodes-1):
		t = random.randint(20, 150)*20
		e = init(t, i, numOfNodes)
		eventList.append(e)


	min_t = 0

	flag = True
	timer = 20
	data = []
	while True:
		if not eventList:
			break
            # This is the simulation result
            #This controls the time for which the simulation will run
		elif min_t > fromSecondToSlot(.5):  # 6250000  # *4/250000
			break
		else:
			min_index, min_t = min(enumerate(e.time for e in eventList),key=operator.itemgetter(1))
			newList = act(eventList[min_index], nodes, 'normal')
			eventList.pop(min_index)
			for n in newList:
				eventList.append(n)

		if min_t > fromSecondToSlot(timer):
			# perform the collection
			temp = []
			for i in range(numOfNodes-1):
				temp.append(nodes[i].getChannelIndicators(450, 160))


			data.append(temp)
			# and set the condition
			timer += 10
		
	# writer = csv.writer(open('data3.csv', 'w'))
	#
	# for eachData in data:
	# 	writer.writerow([eachData[0][0], 1.0-eachData[0][1]])
	return


def fromSecondToSlot(second):
	return second*250000/4


def fromSlotToSecond(slot):
	return slot*4/250000


for i in range(1, 51): # The number of times the simulation will run
	stats.init()
	start = time.time()
	#Newly added start
	stats.NODES = 10 * i
	simulate(stats.NODES - 1)
	#Newly added finish
	end = time.time()
	stats.TIME = end-start
	print('Time: ',stats.TIME)
	print('Packets Sent: ',stats.PACKETS)
	print('Total Packets: ', stats.TOTAL_PACKETS)

	print('Nodes: ',stats.NODES)
	#=====================Writing results to the file
	with open('throughput.csv', mode='a') as throughput:
		tpw = csv.writer(throughput, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		tpw.writerow([stats.NODES, #Number nodes in each simulation
					  stats.PACKETS, #Packets transmitted in each simulation
					  stats.TOTAL_PACKETS, #Total packets tried by simulation
					  stats.TOTAL_PACKETS-stats.PACKETS , #Dropped packets
					  stats.TIME, #Packet transmission time
					  stats.PACKET_SIZE, #Size of the packets
					  (stats.PACKETS * stats.PACKET_SIZE) / stats.TIME]) #Throughput of the network
	#==============================================



