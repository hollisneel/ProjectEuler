#######
# Too lazy to copy all of the text...
# https://projecteuler.net/problem=6
#######

def sumsqr(num):
	final = 0
	x = 1
	while x <= num:
		final += x*x
		x += 1
	return final

def sqrsum(num):
	final = 0
	x = 1
	while x <= num:
		final += x
		x += 1
	final = final*final
	return final

print sqrsum(100) - sumsqr(100)
