#########################################
#
# Problem 14 on Project Euler
#
#########################################

def sequence(num):
	count = 0
	while num != 1:
		if num%2 == 0:
			num = num/2
			count += 1
		else:
			num = 3*num + 1
			count += 1

	return count
length = 0
maxLen = 0
maxLenNum = 0
for a in range(1,1000001):
	length = sequence(a)
	if length > maxLen:
		maxLen = length
		maxLenNum = a
print maxLenNum, " : ", maxLen
