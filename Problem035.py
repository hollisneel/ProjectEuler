#############################
#
#   Problem 35
#
#############################


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

def circ_primes_under(num_below):
    all_primes = sieve(num_below)
    circ = []
    for a in all_primes:
        is_primes = 0
        prime = str(a)
        for a in range(len(prime)):
            if all_primes.count(int(prime)) != 0:
                is_primes += 1
            prime = prime[1:len(prime)] + prime[0]
        if is_primes == len(prime):
            circ.append(int(prime))

    return circ
