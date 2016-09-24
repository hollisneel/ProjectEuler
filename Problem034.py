#############################
#
#   Problem 34
#
#############################

def fact(n):
    s = 1
    for a in range(1,n+1):
        s = s*a
    return s

def prob34():
    final = []
    for a in range(3,1000000):
        prod = 0
        for b in str(a):
            prod = prod + fact(int(b))
        if prod == a:
            final.append(a)
    return final
    
