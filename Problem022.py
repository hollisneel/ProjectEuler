##################################################
#
# Problem 22 from Project Euler
#
##################################################

def readCSVtoList(filename):
	f = open(filename,'r')
	lines = f.readline()
	f.close()
	lines = lines.replace('"',"")
	lines = lines.replace(" ","")
	commaPos = [-1]
	final_list = ["",]
	for check in range(len(lines)):
		if lines[check] == ",":
			commaPos.append(check)
	for to_lst in range(len(commaPos)):
		if to_lst+1 < len(commaPos):
			final_list.append(lines[commaPos[to_lst]+1:commaPos[to_lst+1]])
		else:
			final_list.append(lines[commaPos[to_lst]+1:len(lines)])
	final_list.sort()
	return final_list

def valueOfName(name,index=1):
	name = name.upper()
	alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	value = 0
	for pos1 in range(len(name)):
		tempval = alphabet.index(name[pos1])
		value += tempval
		print name[pos1]," : ",tempval
	final = value*(index)
	print "Index : ", index, 
	print value
	return final

val = 0
files = readCSVtoList("p022_names.txt")
#files = readCSVtoList("test.txt")
for check in range(len(files)):
	tempval = valueOfName(files[check],check)
	val += tempval

print val
