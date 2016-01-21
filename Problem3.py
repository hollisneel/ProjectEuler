#########
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143
#######

number = 600851475143
currentFactor = number
x = 1
while x < currentFactor:
	if currentFactor%x == 0:
		currentFactor = currentFactor/x
	x += 1
print currentFactor
