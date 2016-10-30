#############################
#
#   Problem 49
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

def permutations(lst):
    elements = range(0,len(lst))
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

    lst_perms = []
    for a in perms:
        temp = []
        for b in a:
            temp.append(lst[b])
        lst_perms.append(temp)
    return lst_perms

def is_prime(num,pms=-1):
    if pms == -1:
        pms = sieve(int(math.sqrt(int(num))))
    for a in pms:
        if num%a == 0:
            return 0
    return 1


def prime_pandig_lin(x = 1000,y=10000):
    n = 4
    final = set()
    for a in range(x,y):
        lst = []
        for b in str(a):
            lst.append(b)
    
        perms = permutations(lst)

        nums = []
        for b in perms:
            num = ''
            for c in b:
                num += c
            nums.append(int(num))
        nums.sort()
        all_val = []
        for b in range(len(nums)):
            val = []
            for c in range(len(nums)):
                if c <= b:
                    continue
                if nums.count(nums[b] + (nums[c]-nums[b])*2) == 1 and nums[c] - nums[b] != 0 and all_val.count([nums[b],nums[c],nums[b]+(nums[c]-nums[b])*2]) == 0:   
                    val.append([nums[b],nums[c],nums[b]+(nums[c]-nums[b])*2])
            if len(val) != 0:
                val.sort()
                all_val += val
 
        for b in all_val:
            count = 0
            for c in b:
                if is_prime(c) and c > 1000:
                    count += 1
            if count == len(b):
                print b
                final.add(tuple(b))
    return final  



def is_perm(lst):
    p = -1
    for a in range(len(lst)):
        lst[a] = str(lst[a])
        l = len(lst[a])
        if p != -1 and p != l:
            return 0
        p = l
    for a in lst:
        for c in lst:
            for b in a:
                if c.find(b) == -1:
                    return 0
    return 1


def try_2():
    pms = sieve(10000)
    fdp = []
    for a in pms:
        if len(str(a)) == 4:
            fdp.append(a)
    final = []
    fdp.sort()
    fdp_s = set(fdp)
    for a in range(len(fdp)):
        for b in range(len(fdp)):
            if b <= a:
                continue 
            num1 = fdp[a]
            num2 = fdp[b]
            num3 = fdp[b] + (num2-num1)
            if is_perm([num1,num2,num3]) and len(fdp_s.intersection({num3})) != 0:
                final.append((num1,num2,num3))
    return final
 
            
    


 
