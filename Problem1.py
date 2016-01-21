######################
# If we list all the natural numbers below 10 that are multiples 
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
######################
sum = 0
mult3 = 3
mult5 = 5
allmult = []
loop = 1


while mult3 < 1000:
	mult3 = 3 * loop
	if mult3 < 1000:
		allmult.append(mult3)
	loop += 1

print "Finished all multiples of 3"

loop = 1
while mult5 < 1000:
	mult5 = 5 * loop
	if mult5 < 1000 and allmult.count(mult5) == 0:
		allmult.append(mult5)
	loop += 1

print "Finished all multiples of 5"

sum = 0
for item in range(len(allmult)):
	sum = sum + allmult[item]

print sum
