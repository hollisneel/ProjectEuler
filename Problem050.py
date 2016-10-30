#############################
#
#   Problem 50 :)
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

def pm_sum(num_below,mx_len=0):
    pms = sieve(num_below)
    pms_s=set(pms)
    pms.sort()
    f = []
    
    for start in range(len(pms)):
        val = pms[start]
        lst = [pms[start]]
        for end in range(start+1,len(pms)):
            val += pms[end]
            lst.append(pms[end])
            length = len(lst)

            if len(pms_s.intersection({val})) != 0:
                f.append((length,val))
    f.sort()
    return f

def pm_2(num_below,mx_int):
    pms = sieve(num_below)
    pms_s=set(pms)
    pms.sort()
    f = []
    s = len(pms)

    for start in range(0,3):
        sm = 0
        for end in range(s-start-mx_int):
            if s-end < start or mx_int > s-end-start:
                break
            lst = pms[start:len(pms)-end]
            val = sum(lst)
            lng = len(lst)
            if len(pms_s.intersection({val})) != 0:
                f.append((lng,val))
                if mx_int < lng:
                    mx_int = lng
                break
        if s - start < mx_int:
            break
    return f

def pm3(num_below):
    pms = sieve(num_below)
    ut = 0
    lt = 0
    lg_gap = 0
    sm_lst = []
    sm = 0
    for a in pms:
        sm += a
        sm_lst.append(sm)
          
    return sm_lst

    


