#################################################
#
# Problem 21 from Project Euler
#
#################################################
import math
def findDivisors(num):
	divisors = [1,]
	primec = 2
	mult = 1	
	while primec*mult < num and primec*mult != num:
		if divisors.count(primec*mult) == 0 and num%(primec*mult)==0:
			divisors.append(primec*mult)
		mult += 1

	primec +=1
	sqrt = math.sqrt(num)
	while primec <= int(num/2)+1:
		mult = 1
		while primec*mult< num and primec*mult != num:
			if divisors.count(primec*mult) == 0 and num%(primec*mult)==0:
				divisors.append(primec*mult)
			mult += 1
		primec += 2
	divisors.sort()
	return divisors

def findAmicableNumUnder(num):
	amicableNum = []
	amicableSingle = []
	for a in range(1,num+1):
		divlist = findDivisors(a)
		summ = 0
		for b in range(len(divlist)):
			summ += divlist[b]
		divlist2 = findDivisors(summ)
		summ2 = 0
		for c in range(len(divlist2)):
			summ2 += divlist2[c]
		if summ2 == a and a != summ and amicableSingle.count(a) == 0:
			amicableNum.append([a,summ])
			amicableSingle.append(a)
			amicableSingle.append(summ)

	return amicableNum

a = findAmicableNumUnder(10000)
summ = 0
for b in range(len(a)):
	for c in range(2):
		summ += a[b][c]

print summ
