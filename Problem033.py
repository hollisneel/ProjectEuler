#############################
#
#   Problem 33 
#
#############################


def find_weird_two_digit_fractions():
    lst = []
    for num in range(10,100):
        for den in range(10,100):
            if num > den:
                continue

            if check(num,den):
                lst.append((num,den))
    return lst


def check(num,den):

    if num != den and str(num)[0] != str(num)[1] and((str(den)[0] != '0' and float(num)/den == float(str(num)[1])/float(str(den)[0])) or (str(den)[1] != '0' and float(str(num)[0])/float(str(den)[1]) == float(num)/den)) and (str(num)[0] == str(den)[1] or str(num)[1]==str(den)[0]):
        return True
    return False


def final():
    tups = find_weird_two_digit_fractions()
    num = 1
    den = 1
    for a in range(len(tups)):
        num = num*tups[a][0]
        den = den*tups[a][1]
    print num,den
    for a in range(2,den):
    
        while num%a==0 and den%a == 0:
            num = num/a
            den = den/a
    return(num,den)
