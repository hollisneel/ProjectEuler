#############################
#
# Problem 36
#
#############################
import math

def num_to_base(num,base):
    sub = int(num)
    highest_pow = int(math.log(num,base))
    pows = range(highest_pow+1)
    pows.reverse()
    num = ''
    for a in pows:
        digit = 0
        while base**a <= sub:
            digit += 1
            sub = sub-base**a
        num += str(digit)
    return int(num)



    return bin_list

def is_palindrome(num):
    lst1 = list(str(num))
    lst2 = list(lst1)
    lst2.reverse()
    if lst1 == lst2:
        return 1
    return 0

def palindromes_under(num, bases=[10]):
    pals = []
    for a in range(1,num+1):
        count = 0
        for b in bases:
            n = num_to_base(a,b)
            if not is_palindrome(n):
                break
            count += 1
        if count == len(bases):
            pals.append(a)

    return pals





