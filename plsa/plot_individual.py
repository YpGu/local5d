import matplotlib.pyplot as plt
import random
import math
import sys

# plot the average idp of R/D's in each congress 
def plotidp(inDir, outDir):
	print 'Be sure to modify topics accordingly!'
	vs = {}; years = []
	labels = ['Crime', 'Tax', 'Health Care', 'Foreign', 'Energy']
	fin = open(inDir)
	lines = fin.readlines()
	num_years = len(lines)
	K = len(lines[0].split('\t')) - 1
	print str(K) + ' topics'
	for k in range(K):
		vs[k] = []
	for line in lines:
		ls = line.split('\t')
		year = ls[0]
		for k in range(K):
			vs[k].append(float(ls[k+1]))
		years.append(1788 + 2 * int(year))
	fin.close()

	fig = plt.figure()
	line_0, = plt.plot(years, vs[0], 'r-', label = 'Topic 0')
	plt.scatter(years, vs[0], c = ['r' for x in years], label = 'Topic 0')
	line_1, = plt.plot(years, vs[1], 'b-', label = 'Topic 1')
	plt.scatter(years, vs[1], c = ['b' for x in years], label = 'Topic 1')
	line_2, = plt.plot(years, vs[2], 'g-', label = 'Topic 2')
	plt.scatter(years, vs[2], c = ['g' for x in years], label = 'Topic 2')
	line_3, = plt.plot(years, vs[3], 'c-', label = 'Topic 3')
	plt.scatter(years, vs[3], c = ['c' for x in years], label = 'Topic 3')
	line_4, = plt.plot(years, vs[4], 'm-', label = 'Topic 4')
	plt.scatter(years, vs[4], c = ['m' for x in years], label = 'Topic 4')
	
#	plt.xlim([103,120])
	plt.xlim([1945,2030])
	plt.legend([line_0, line_1, line_2, line_3, line_4], labels, loc = 1)
	fig.savefig(outDir)
	plt.show()
	sys.exit()

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print 'Usage: python plot_individual.py <input> <output>'
		print '\tor: python plot_individual.py <option> (1 for soft; 2 for hard)'
		print 'Example: python plot_individual.py year_stat_soft.txt year_topics_soft.png'
	elif len(sys.argv) == 2:
		if int(sys.argv[1]) == 1:
			plotidp('./year_stat_soft.txt', 'year_topics_soft.png')
		if int(sys.argv[1]) == 2:
			plotidp('./year_stat_hard.txt', 'year_topics_hard.png')
	elif len(sys.argv) == 3:
		plotidp(sys.argv[1], sys.argv[2])
	else:
		print 'Invalid argument list.'

