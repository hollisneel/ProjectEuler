##############################
#
# Project Euler Problem 23
#
##############################

def abundantNumsUnder(num):
	abundantNum = []
	for a in range(1,num+1):
		if isAbundant(a):
			abundantNum.append(a)
		print a
	return abundantNum


def isAbundant(num):
	div = factors(num)
	summ = 0
	for a in range(len(div)):
		summ += div[a]
	if summ >= num:
		return 1
	else :
		return 0

def factors(num):
	factors = []
	for a in range(1,int(num/2)+1):
		if num%a == 0:
			factors.append(a)
	return factors

abundantSums = abundantNumsUnder(10000)

All = range(1,10000)
sums = []
abundantSums.append(0)
total = 0
for a in range(len(abundantSums)):
	for b in range(a,len(abundantSums)):
		sums.append(abundantSums[a]+abundantSums[b])
	print a, len(abundantSums)
print "finished summing"
for a in range(len(sums)):
	if All.count(sums[a]) > 0:
		All.remove(sums[a])
	print a, len(sums)
print "finished Polishing"
for a in range(len(All)):
	total += All[a]
print All
print total












