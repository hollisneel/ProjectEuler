###################################
#
# Problem 20 Project Euler
#
###################################

def sumDigits(num,power = 1):
	numStr = str(num**power)
	sumDigits = 0
	for a in range(len(numStr)):
		sumDigits += int(numStr[a])
	return sumDigits

def factorial(num):
	product = 1
	while num >1:
		product *= num
		num += -1
	return product
