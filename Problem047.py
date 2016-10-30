#############################
#
#   Problem 47
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

def num_factors(n,consec,lim):
    pms = sieve(lim)
    num = 2
    cons = 0
    pot_num = []
    facts = set()
    nums = []
    while consec != cons:
        temp = int(num)
        facts = set()
        for a in pms:
            while temp%a == 0:
                temp = temp/a
                facts.add(a)
            if temp == 1:
                break

        if len(facts) == n:
            cons += 1
            nums.append(num)
        if len(facts) != n and cons != 0:
            cons = 0
            nums = []
        if cons == consec:
            return nums
        num += 1
