#############################
#
# Problem 37
#
#############################

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

def two_sided_primes():
    primes = sieve(1000000)
    p_set  = set(primes)
    tsp = []
    for a in primes:
        num = int(a)
        for b in range(len(str(a))):
            if len(p_set.intersection({int(str(a)[b:len(str(a))])}))==0:
                 break
            if len(p_set.intersection({int(str(a)[0:len(str(a))-b])}))==0:
                break 
            if b == len(str(a))-1:
                tsp.append(a)
    return tsp 
