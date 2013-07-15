import urllib2
RESULT = range(11)

print "01: RESULT len:" + str(len(RESULT))

def Test():
	global RESULT
	total = RESULT[:]
	result = []
	for i in total:
		if i % 2 == 0:
			result.append(i)
			total.remove(i)
	print "02: total len:" + str(len(total))
	print "03: RESULT len:" + str(len(RESULT))	

Test()
