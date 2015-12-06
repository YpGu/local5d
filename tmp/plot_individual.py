import matplotlib.pyplot as plt
import random
import math
import sys

def vari(arr):
	if len(arr) == 1 or len(arr) == 0:
		return 0
	ave = 0.0
	for a in arr:
		ave += a
	ave /= float(len(arr))
	res = 0.0
	for a in arr:
		res += (a-ave) * (a-ave)
	res /= (float(len(arr)-1))
	return math.sqrt(res)

# plot the average idp of R/D's in each congress 
def plotidp():
	xsr = {}; xsd = {}; ysr = {}; ysd = {}
	fin = open('./idp_case_study.txt')
	candidates_r = {}; candidates_d = {}
	lines = fin.readlines()
	rid = 0; did = 0
	for line in lines:
		ls = line.split('\t')
		newid = int(ls[0])
		party = ls[3].split('\n')[0]
		if party == 'R':
#			candidates_r[newid] = 0
#			rid = len(candidates_r)-1
#			candidates_r[rid] = newid
			if newid not in xsr:
				xsr[newid] = []
				ysr[newid] = []
		elif party == 'D':
#			candidates_d[newid] = 0
#			did = len(candidates_d)-1
#			candidates_d[did] = newid
			if newid not in xsd:
				xsd[newid] = []
				ysd[newid] = []

		year = 1790 + int(ls[1]) * 2
		v = float(ls[2])
		if party == 'R':
			xsr[newid].append(year)
			ysr[newid].append(v)
		elif party == 'D':
			xsd[newid].append(year)
			ysd[newid].append(v)
	fin.close()
	print 'Total number of Republicans = ' + str(len(xsr)) + ' (in position for at least 10 terms)'
	print 'Total number of Democrats = ' + str(len(xsd)) + ' (in position for at least 10 terms)'

	# calculate variance
	variance = {}
	for i in xsr:
		variance[i] = vari(ysr[i])
	for i in xsd:
		variance[i] = vari(ysd[i])
	# sort
	breakCount = 0
	fig = plt.figure()
	breakStart = 0;					# start from this number 
	breakHit = 10;					# top X people with highest variance
	for i in sorted(variance.items(), key = lambda x: x[1], reverse = True):
		newid = i[0]
		if breakCount < breakStart:
			breakCount += 1
			continue
		breakCount += 1
		if breakHit < 30:
			print newid
		if newid in xsr:# and newid == 10744:
			plt.plot(xsr[newid], ysr[newid], 'r:', label = 'Line 1')
			plt.scatter(xsr[newid], ysr[newid], c = ['r' for x in xsr[newid]])
		elif newid in xsd:
			plt.plot(xsd[newid], ysd[newid], 'b:', label = 'Line 2')
			plt.scatter(xsd[newid], ysd[newid], c = ['b' for x in xsd[newid]])
		if breakCount == breakHit:
			break
	plt.xlim([1789,2020])
	fig.savefig('idp_case_study.png')
	plt.show()
	sys.exit()

	number_of_cs = 2
	if False:
		maxid = -1; maxv = 0
		for i in ysr:
			print str(i) + '\t' + str(len(ysr[i])) + '\t' + str(vari(ysr[i]))
			if vari(ysr[i]) > maxv:
				maxv = vari(ysr[i])
				maxid = i
#		maxid = 7
		plt.plot(xsr[maxid], ysr[maxid], 'r:', label = 'Line 1')
		plt.scatter(xsr[maxid], ysr[maxid], c = ['r' for u in ysr[i]], label = 'Line 1s')
		plt.show()
		sys.exit()

	if False:
		maxid = -1; maxv = 0
		for i in ysd:
			print str(i) + '\t' + str(len(ysd[i])) + '\t' + str(vari(ysd[i]))
			if vari(ysd[i]) > maxv:
				maxv = vari(ysd[i])
				maxid = i
		plt.plot(xsr[maxid], ysr[maxid], 'r:', label = 'Line 1')
		plt.scatter(xsr[maxid], ysr[maxid], c = ['r' for u in ysr[i]], label = 'Line 1s')
		plt.show()
		sys.exit()


	startpoint = random.randint(0, min(rid, did) + 1 - number_of_cs)
#	startpoint = 0
	fig = plt.figure()
	for i in range(startpoint, startpoint + number_of_cs):
		line_r = plt.plot(xsr[i], ysr[i], 'r:', label = 'Line 1')
		line_d = plt.plot(xsd[i], ysd[i], 'b:', label = 'Line 2')
		line_rs = plt.scatter(xsr[i], ysr[i], c = ['r' for u in ysr[i]], label = 'Line 1s')
		line_ds = plt.scatter(xsd[i], ysd[i], c = ['b' for u in ysd[i]], label = 'Line 2s')
	plt.xlabel('Year')
	plt.ylabel('Ideal Point')
	plt.xlim([1789,2020])
#	plt.legend([line_r, line_d], ['Republican', 'Democrat'], loc = 2)
	plt.show()
	fig.savefig('idp_case_study.png')


if __name__ == '__main__':
	plotidp()

