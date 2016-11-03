#############################
#
#   Problem 51
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


def dup_dig_prime(lim,nc):
    '''
        lim is the maximum number possibles
    '''
    primes = sieve(lim)
    primes.sort()
    for a in range(len(primes)):
        if len(str(primes[a])) == 4:
            primes = primes[a:len(primes)]
            break
    
    for a in range(len(primes)):
        pm = primes[a]
        if pm == 56003:
            print pm
        pos = []
        for b in range(len(str(pm))):
            if str(pm)[b] == '0':
                pos.append(b)

        if pm == 56003:
            print pos

        if len(pos) >= 2:
            dup = []
            for c in pos:
                for d in pos:
                    if c >= d:
                        continue
                    dup.append([c,d])
            if pm == 56003:
                print dup

            if pm == 56003:
                print dup
            for c in dup:
                pm_l = 0
                for d in range(10):
                    t = str(pm)
                    num = t[0:c[0]] + str(d) + t[c[0]+1:c[1]] + str(d) + t[c[1]+1:len(str(pm))]
                    if len(set(primes).intersection({int(num)})) != 0:
                        pm_l += 1
                if pm == 56003:
                    print pm_l
                if pm_l >= nc:
                    return pm
    return -1


def dup_dig_prime2(num_below,match):

    primes = sieve(num_below)
    primes.sort()

    dups = [] 
    for prime in primes:
        ps = str(prime)
        length = len(ps)
        pos = []
        for a in range(len(ps)):
            if ps[a] == '0':
                pos.append(ps[a])
        print pos
        if len(pos) != 0:
            dups = power_set(pos)
    return dups
            
def power_set(lst):
    num = ''
    length = len(lst)
    power = 1
    print lst 
    top = num_to_base(2**(len(lst))-1,2)
    st = []
    for a in range(1,2**len(lst)):
        temp = num_to_base(a,2)
        string = str(temp)
        while len(string) <len(lst):
            string = '0' + string
        t_l = []
        for a in string:
            t_l.append(int(a))
        st.append(t_l)
    
    final = []
    for perm in st:
        temp = []
        for pos in range(len(perm)):
            if perm[pos]:
                print perm, pos
                temp.append(lst[pos])
        final.append(temp)
    final.sort()
    return final

def num_to_base(num,base):
    sub = int(num)
    highest_pow = int(math.log(num,base))
    pows = range(highest_pow+1)
    pows.reverse()
    num = ''
    for a in pows:
        digit = 0
        while base**a <= sub:
            digit += 1
            sub = sub-base**a
        num += str(digit)
    return int(num)



 


