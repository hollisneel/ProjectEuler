#############################
#
#   Problem 43
#
#############################

def fact(n):
    prod = 1
    for a in range(1,n+1):
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

def pan_div_pos(st,en):
    perm = permutations(st,en+1)
    vals = []
    pas = []
    for a in perm:
        vl = ''
        for b in a:
            vl += str(b)
        vals.append(vl)

    for a in vals:
        t = 0
        if int(a[1:4])%2 == 0:
            t += 1
        if int(a[2:5])%3 == 0:
            t += 1
        if int(a[3:6])%5 == 0:
            t += 1
        if int(a[4:7])%7 == 0:
            t += 1
        if int(a[5:8])%11 == 0:
            t += 1
        if int(a[6:9])%13 == 0:
            t += 1
        if int(a[7:10])%17 == 0:
            t += 1

        if t == 7:
            pas.append(int(a))

    return sum(pas)




    




