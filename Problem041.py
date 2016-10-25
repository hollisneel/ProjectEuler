#############################
#
#   Problem 41
#
#############################
import math

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

def fact(num):
    prod = 1
    for a in range(1,num+1):
        prod = prod*a
    return prod

def permutations(start,end_plusone):
    elements = range(start,end_plusone)
    perms = []
    elmt_depth = len(elements) -1
    for a in range(fact(len(elements))):
        perms.append([])
    for a in range(len(elements)):
        iters = fact(elmt_depth)
        pos = 0
        count = 0
        for b in range(len(perms)):
            tmp = list(elements)
            for c in perms[b]:
                tmp.remove(c)
            perms[b].append(tmp[pos])
            count += 1
            if elmt_depth != 0 and count % iters == 0 and len(elements)-a != 0:
                pos = (pos + 1)%(len(elements)-a)
        elmt_depth += -1
    return perms

def is_prime(num,pms=-1):
    if pms == -1:
        pms = sieve(int(math.sqrt(num)))
    for a in pms:
        if num%a == 0:
            return 0
    return 1

def pan_prime(n):   
    pans = permutations(1,n)
    pans.reverse()
    for a in pans:
        num = ''
        for b in a:
            num += str(b)
        n = int(num)
        if is_prime(n):
            return n








