#############################
#
#   Problem 30
#
#############################
 
# Will choose a "flow down" method in which we will create a list
# of ALL lists. In a sorted list we start by creating a list of 
# all values until it goes over the desired value (where it stops..)
    
def coins_sum_to(coin_list, value):
    if type(coin_list) != list:
        return "Not a Coin List..."
    
    coin_list.sort()
    coin_list.reverse()

    mst = [[]]
    
    for coin in coin_list:
        full_list = []
        
        for lst in mst:
            while sum(lst) <= value:
                full_list.append(list(lst))
                lst.append(coin)
        mst = full_list
    
    final = []
    for a in mst:
        if sum(a) == value:
            final.append(a)
        
    return final

