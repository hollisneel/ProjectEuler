#############################
#
#   Problem 44
#
#############################

def pent_num(n):
    return n*(3*n-1)/2

def min_diff(num):
    pents = []
    for a in range(1,num):
        pents.append(pent_num(a))
    pent = set(pents)
    diff = 1000
    diffs = []

    for i in range(len(pents)):
        for j in range(len(pents)):
            if j >= i:
                continue
            if len(pent.intersection({pents[i] + pents[j]})) != 0 and len(pent.intersection({abs(pents[i] - pents[j])})) != 0: 
                diffs.append(abs(pents[i]-pents[j]))
    return min(diffs)
     




