#############################
#
#   Problem 48 
#
#############################

def series(start,stop):
    num = 0
    for a in range(start,stop+1):
        num += a**a
    return num

