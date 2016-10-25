#############################
#
#  Problem 39
#
#############################

def pythag_triples(lim):
    trips = set()
    
    for m in range(1,lim):
        for n in range(1,lim):
            if n >= m:
                continue
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            mult = 1
            while mult*(a + b + c) <= lim:
                st = [mult*a,mult*b,mult*c]
                st.sort()
                st = tuple(st)
                trips.add(st)
                mult += 1


    return list(trips)

def perimeter(lim):
    trips = pythag_triples(lim)
    dic = {}
    for a in trips:
        P = a[0]+a[1]+a[2]
        if dic.has_key(P):
            dic[P] += 1

        else:
        
            dic[P] = 1

    return dic        

def prob_39(lim):
    dic = perimeter(lim)
    mx = 0
    mx_val = 0
    for a in dic.keys():
        if dic[a] >mx_val:
            mx = a
            mx_val = dic[a]

    return mx

            
