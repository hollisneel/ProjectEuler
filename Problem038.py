#############################
#
# Problem 38
#
#############################

def is_pandigital(num,lst):
    string = str(num)
    if len(string) != lst[1]-lst[0]+1:
        return 0

    for a in range(lst[0],lst[1]+1):
        if string.count(str(a)) != 1:
            return 0
    return 1


def find_pan(rnge,num_top):
    start = rnge[1]
    end   = rnge[0]
    size = start-end+1
    pans = []
    print size
    for a in range(10,num_top):
        pot = ''
        mult = 1
        num =''
        while len(pot) + len(str(a*mult)) <= size:
            num = str(a*mult)
            mult += 1
            pot += num
        if pot != '' and is_pandigital(int(pot),rnge):
            pans.append((a,mult-1,int(pot)))

    return pans 
