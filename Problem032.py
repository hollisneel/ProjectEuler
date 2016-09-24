#############################
#
#   Problem 32
#
#############################

# Since we are pandigital, It must be one of the following cases:
#   1) x  *  yyyy = zzzz    1 <= x < 10 | 1000 <= y < ceil(10000/x)
#   2) xx *  yyy  = zzzz   10 <= x < 100| 100  <= y < ceil(10000/x)

def is_pandigital(string,rnge):
    string = str(string)
    if len(string) != len(range(rnge[0],rnge[1])):
        return False
    for a in range(rnge[0],rnge[1]):
        if string.count(str(a)) == 0 or string.count(str(a)) >1 :
            return False
    return True

def permutations(start,end_plusone):
    elements = range(start,end_plusone)

    perms = []
    elmt_depth = len(elements) -1


    for a in range(fact(len(elements))):
        perms.append([])

    for a in range(len(elements)):

        iters = fact(elmt_depth)
        pos = 0
        count = 0

        for b in range(len(perms)):
            
            tmp = list(elements)
            for c in perms[b]:
                tmp.remove(c)
            
            perms[b].append(tmp[pos])
            count += 1
            if elmt_depth != 0 and count % iters == 0 and len(elements)-a != 0:
                pos = (pos + 1)%(len(elements)-a)

        elmt_depth += -1
    return perms



def fact(num):
    if num == 0 or num == 1:
        return 1
    n = 1
    for a in range(1,num+1):
        n = n*a
    return n

def pandig_prod_search(rnge):
    perms = permutations(rnge[0],rnge[1])
    
    interesting = []
    chk = [] 
    used_mults = []
    used_prods = []
    for a in perms:

        for pos1 in range(rnge[0],rnge[1]):
            for pos2 in range(rnge[0],rnge[1]):
                if pos1 > pos2:
                    continue
                
                if abs(pos1-pos2) <1:
                    continue
 
                num1 = ''
                num2 = ''
                num3 = ''

                
                for b in a[0:pos1]:
                    num1 += str(b)
                for c in a[pos1:pos2]:
                    num2 += str(c)
                for d in a[pos2:len(a)]:
                    num3 += str(d)
                
                used_mults.append((num1,num2))


                if num1.isdigit() and num2.isdigit() and num3.isdigit() and str(int(num1)*int(num2)) == num3 and used_mults.count((num2,num1)) == 0 and used_prods.count(num3) == 0:
                    interesting.append(int(num3))
                    chk.append((num1,num2,num3))
                    used_prods.append(num3)
    return chk, sum(interesting)











