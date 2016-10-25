############################
#
#   Problem 35
#
#############################
import math, random

def sieve(num_below):
    pot = range(num_below+1)

    for a in range(len(pot)):
        num = pot[a]
        if num != 0 and num != 0 and num != 1:
            mult = 2
            while num*mult < len(pot):
                pot[num*mult] = 0
                mult += 1
    return list(set(pot))[2:len(pot)]

def circular_prime(num_under):
    plist = sieve(num_under)
    
    p_set = set(plist)
    c_primes = set()
    for a in plist:
        pot = str(a)
        count = 0
        for b in range(len(pot)):
            if len(p_set.intersection({int(pot)})) == 1:
                count += 1
            if len(p_set.intersection({int(pot)})) == 0:
                continue 
            pot = pot[1:len(pot)] + pot[0]
        if count == len(pot):
            c_primes.add(a)

    return list(c_primes)
                     

