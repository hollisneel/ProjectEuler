####################
#
# Project Euler Problem 10
#
####################

def sum_primes_below(num_below):
	primes_below = range(2,num_below+1)
	loop_bool = 1
	All_primes_bool = 1
	list_index = 0
	count = 0


	while All_primes_bool:
		prime = primes_below[list_index]
		index2 = list_index + 1
		mult = 2
		num = prime*mult
		while num <= num_below and num != 0:
			primes_below[num-2] = 0
			mult += 1
			num   = mult*prime
		list_index += 1
		if list_index == len(primes_below):
			All_primes_bool = 0	
	
	summ = 0

	for x in range(len(primes_below)):
		summ += primes_below[x]
	print summ
	return summ	

a = sum_primes_below(10000000)
