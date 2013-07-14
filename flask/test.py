import time

GLO = time.time()

def Test():
	print GLO
	temp = time.time();
	print temp
	GLO = temp

Test()
