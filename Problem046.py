#############################
#
#   Problem 46
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



def squares(num_below):
    a = 0
    lst = []
    while a**2 < num_below:
        lst.append(a**2)
        a += 1
    return lst


def golbach_wrong(num_below):
    lst = range(num_below)
    pms = sieve(num_below)
    sqr = squares(num_below)

    for a in pms:
        for b in sqr:
            num = a + 2*b
            if num < num_below:
                lst[num] = 0

    for a in range(len(lst)):
        if lst[a]%2 == 0:
            lst[a] = 0
    return set(lst)

