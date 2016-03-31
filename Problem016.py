#########################################
#
# Problem 16 from Project Euler
#
#########################################

def sumDigits(num,power = 1):
	numStr = str(num**power)
	sumDigits = 0
	for a in range(len(numStr)):
		sumDigits += int(numStr[a])
	return sumDigits
