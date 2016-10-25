#############################
#
#   Problem 45
#
#############################

def tri_num(n):
    return n*(n+1)/2
def pent_num(n):
    return n*(3*n-1)/2
def hex_num(n):
    return n*(2*n-1)

def sims(test_under):
    tri = []
    pent= set()
    hx  = set()
    for a in range(1,test_under):
        tri.append(tri_num(a))
        pent.add(pent_num(a))
        hx.add(hex_num(a))
    fn = []
    for a in tri:
        if len(pent.intersection({a})) != 0 and len(hx.intersection({a})) != 0 :
           fn.append(a)

    return fn 


















