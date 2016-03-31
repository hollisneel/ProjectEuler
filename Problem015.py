################################
#
# Problem 15 on Project Euler
#
#################################
import math
# Copying Pascals Triangle...
def numberOfPaths(sqrGrd):
	num = math.factorial(2*sqrGrd)/(math.factorial(sqrGrd)*math.factorial(sqrGrd))
	
	return num
