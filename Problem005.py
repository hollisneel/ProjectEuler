#####################
# 2520 is the smallest number that can be divided by each of the
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by
# all of the numbers from 1 to 20?
#####################

# Since it must be divisible by every number 1-20 and
# primes are the building blocks, lets use all the primes
# whose powers are <= 20..
 
answer = 2*2*2*2*3*3*5*7*11*13*17*19
print answer
