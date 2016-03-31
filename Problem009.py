########################
#
# Project Euler Problem 9
#
########################

# a^2 + b^2 = c^2
# a + b + c = 1000
#
# a + b + sqrt(a2+b2) = 1000
# a + b -1000 = sqrt(a2+b2)
# a2 + ab -1000a + ab + b2 -1000b -1000a -1000b +10.0 1000000 = a2 + b2
# 2ab - 2000a - 2000b + 1000000 = 0
# 1000000 - 2000b = 2a(b - 1000) 
# 500000/(b - 1000) - 1000/(b-1000) = a
# b = 
# a = 
k = 1
a = 0
b = 0
c = 0
y = 0.0
triples = []
acomp = 0
bcomp = 0
ccomp = 0
acomp2 = 0
bcomp2 = 0
ccomp2 = 0
for m in range(1,250):
	for n in range(1,m+1):
		acomp = m*m-n*n
		bcomp = 2*m*n
		ccomp = m*m+n*n
		acomp2 = acomp
		bcomp2 = bcomp
		ccomp2 = ccomp
		k = 1
		while acomp2 + bcomp2 +ccomp2 <= 1000:
			acomp2 = k*acomp
			bcomp2 = k*bcomp
			ccomp2 = k*ccomp
			k+=1
			if acomp2+bcomp2+ccomp2 == 1000:
				triples.append([acomp2,bcomp2,ccomp2,acomp2+bcomp2+ccomp2])
				break
		triples.append([acomp2,bcomp2,ccomp2,acomp2+bcomp2+ccomp2])
for x in range(len(triples)):
	if triples[x][3] == 1000 and triples[x][0] != 0 and triples[x][1] != 0 and triples[x][2] != 0:
		a = triples[x][0]
		b = triples[x][1]
		c = triples[x][2]

print" a = ", a
print" b = ", b
print" c = ", c
print ""
print "Product abc = ", a*b*c
