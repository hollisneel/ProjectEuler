############
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
#
# What is the 10001st prime number?
############

def sieve(num_below):
	primelist = range(2,num_below)
	check = 0
	x = 2
	while x < len(primelist):
		y = 2
		while x*y < num_below:
			if primelist.count(x*y) != 0:
				primelist.remove(x*y) 
			y += 1
			if check%10000 == 0:
				print check
			check += 1
		x += 1
	print len(primelist)
	return primelist

a = sieve(100500)
print a[10000]
