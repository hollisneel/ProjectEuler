####################
#
# Problem 12 Project Euler
#
####################

def triangleNum(num):
	return num*(num+1)/2

def findNumDivisors(num):
	count = 0
	if num%2 == 0:
		num = num/2
		count +=1
	div = 1
	while num%2 == 0:
		count += 1
		num = num/2
	div = div*(count+ 1)
	potPrimeDiv = 3
	while num != 1:
		count = 0
		while num%potPrimeDiv == 0:
			count += 1
			num = num/potPrimeDiv
		div = div*(count+1)
		potPrimeDiv += 2
	return div
def hardFactors(num):
	count = 0
	for a in range(1,num+1):
		if num%a == 0:
			count += 1
	return count

def findNumTriDivisors(num):
    count = 0
    if num%2 == 0:
        num = num/2
    div = 1
    while num%2 == 0:
        count += 1
        num = num/2
    div = div*(count+ 1)
    potPrimeDiv = 3
    while num != 1:
        count = 0
        while num%potPrimeDiv == 0:
            count += 1
            num = num/potPrimeDiv
        div = div*(count+1)
        potPrimeDiv += 2
    return div
def hardFactors(num):
    count = 0
    for a in range(1,num+1):
        if num%a == 0:
            count += 1
    return count

def triangularFactorsLEQ(num):
	n = 1
	leftNum = findNumTriDivisors(n)
	rightNum = findNumTriDivisors(n+1)
	while leftNum*rightNum <= num:
		n += 1
		leftNum = rightNum
		rightNum = findNumTriDivisors(n+1)
	return n

b = triangleNum(triangularFactorsLEQ(500))
print b
