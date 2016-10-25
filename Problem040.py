#############################
#
# Problem 40
#
#############################



def irr_dec(length):
    count = 1
    string = '.'
    while len(string)< length+1:
        string = string + str(count)
        count += 1
    return string

def prod_irr(lst_positions):
    length = max(lst_positions)
    irr = irr_dec(length)
    prod = 1
    for a in lst_positions:
        prod = prod*int(irr[a])
    return prod
