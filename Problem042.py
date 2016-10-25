#############################
#
#   Problem 42
#
#############################

def word_to_num(word):
    dic = {"a":1,"A":1,"b":2,"B":2,"c":3,"C":3,"d":4,"D":4,"e":5,"E":5,"f":6,"F":6,"g":7,"G":7,"h":8,"H":8,"i":9,"I":9,"j":10,"J":10,"k":11,"K":11,"l":12,"L":12,"m":13,"M":13,"n":14,"N":14,"o":15,"O":15,"p":16,"P":16,"q":17,"Q":17,"r":18,"R":18,"s":19,"S":19,"t":20,"T":20,"u":21,"U":21,"v":22,"V":22,"w":23,"W":23,"x":24,"X":24,"y":25,"Y":25,"z":26,"Z":26 }
    summ = 0
    for a in word:
        summ += dic[a]
    return summ

def tri_num(n):
    return (n*(n+1))/2

def num_tri_nums(w_list):
    tri_nums= 0
    tri_num_s = set()
    max_tri = 0
    n       = 0
    for a in w_list:
        num = word_to_num(a)
        while num > max_tri:
            n += 1
            max_tri = tri_num(n)
            tri_num_s.add(max_tri)
        if len(tri_num_s.intersection({num})) != 0:
            tri_nums += 1

    return tri_nums

def file_to_list(filepath):

    z = open(filepath)
    raw = z.read()
    z.close()
    raw = raw.replace('"',"")
    lst = raw.split(",")

    return lst





    




