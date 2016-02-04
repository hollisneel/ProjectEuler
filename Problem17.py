#########################################
#
# Problem 17 Project Euler
#
#########################################

def numToWords(num):
	
	num = str(num)
	while len(num)<12:
		num = "0" + num
	one       = "one "
	two       = "two "
	three     = "three "
	four      = "four "
	five      = "five "
	six       = "six "
	seven     = "seven "
	eight     = "eight "
	nine      = "nine "
	ten       = "ten "
	eleven    = "eleven "
	twelve    = "twelve "
	thirteen  = "thirteen "
	fourteen  = "fourteen "
	fifteen   = "fifteen "
	sixteen   = "sixteen "
	seventeen = "seventeen "
	eighteen  = "eighteen "
	nineteen  = "nineteen "
	twenty    = "twenty-"
	thirty    = "thirty-"
	fourty    = "forty-"
	fifty     = "fifty-"
	sixty     = "sixty-"
	seventy   = "seventy-"
	eighty    = "eighty-"
	ninety    = "ninety-"
	hundred   = "hundred "
	thousand  = "thousand "
	million   = "million "
	billion   = "billion "
	
	numName    = ""
	
	ones, one1, one2, one3 = 11, 8,5,2
	tens, ten1, ten2, ten3 = 10,7,4,1
	hund,hund1,hund2,hund3= 9,6,3,0

	leftmost_digit_place = len(num)
	num_digits = len(num)
	actual_index = 0
	# ones      = 1 digit
	# tens      = 2 digits
	# hundreds  = 3 digits
	# thousands = 4 digits
	# millions  = 7 digits
	# billions  = 10 digits

	# What's the algorithm for saying numbers out loud?
	#
	# we start by reading the leftmost digit and count the number of spaces to that digit. Then if it's in the relative hundreds
	# place we call out the number followed by hundred. Next, we look at the next digit. If it is one, we look at the next digit as well
	# and call out its name. If not, we refer to the tens list and call out that version of the value. Next(if not done so already), we
	# look at the ones place. we then call out the specific name of the number followed by the group it is in. If the index's place is 1-3
	# digits, we end the loop. If the idex place is 4 we end with thousand, 7 -> million, 10 -> billion.

	while actual_index <= len(num)-1:
		if num_digits >= 13:
			print "Number too large"
			return ""
		#Billions
		if actual_index == hund3:
			if num[actual_index] == "1":
				numName += one
				actual_index += 1
				continue 
			if num[actual_index] == "2":
				numName += two
			if num[actual_index] == "3":
				numName += three
			if num[actual_index] == "4":
				numName += four
			if num[actual_index] == "5":
				numName += five
			if num[actual_index] == "6":
				numName += six
			if num[actual_index] == "7":
				numName += seven
			if num[actual_index] == "8":
				numName += eight
			if num[actual_index] == "9":			
				numName += nine
			if num[actual_index] != "0":
				numName += hundred
				if num[actual_index:len(num)].count("0") != len(num):
					numName += "and "
		if actual_index == ten3:
			if num[actual_index:actual_index+2] ==  "10":
				numName += ten
			if num[actual_index:actual_index+2] ==  "11":
				numName += eleven + billion
			if num[actual_index:actual_index+2] == "12":
				numName += twelve + billion
			if num[actual_index:actual_index+2] == "13":
				numName += thirteen + billion
			if num[actual_index:actual_index+2] == "14":
				numName += fourteen + billion
			if num[actual_index:actual_index+2] == "15":
				numName += fifteen + billion
			if num[actual_index:actual_index+2] == "16":
				numName += sixteen + billion
			if num[actual_index:actual_index+2] == "17":
				numName += seventeen + billion
			if num[actual_index:actual_index+2] == "18":
				numName += eighteen + billion
			if num[actual_index:actual_index+2] == "19":
				numName += nineteen + billion
			if num[actual_index] == "2":
				numName += twenty
			if num[actual_index] == "3":
				numName += thirty
			if num[actual_index] == "4":
				numName += fourty
			if num[actual_index] == "5":
				numName += fifty
			if num[actual_index] == "6":
				numName += sixty
			if num[actual_index] == "7":
				numName += seventy
			if num[actual_index] == "8":
				numName += eighty
			if num[actual_index] == "9":
				numName += ninety
		if actual_index == one3 and num[actual_index-1] != "1":
			if num[actual_index] == "1":
				numName += one 
			if num[actual_index] == "2": 
				numName += two 
			if num[actual_index] == "3":
				numName += three 
			if num[actual_index] == "4":
				numName += four
			if num[actual_index] == "5":
				numName += five
			if num[actual_index] == "6":
				numName += six 
			if num[actual_index] == "7":
				numName += seven
			if num[actual_index] == "8":
				numName += eight
			if num[actual_index] == "9":
				numName += nine 
			if num[actual_index] != "0" or num[actual_index-1] != "0" or num[actual_index-2] != "0":
				numName += billion
				print actual_index,num[actual_index],num[actual_index-1],num[actual_index-2]
		# Millions
		if actual_index == hund2:
			if num[actual_index] == "1":
				numName += one
			if num[actual_index] == "2":
				numName += two
			if num[actual_index] == "3":
				numName += three
			if num[actual_index] == "4":
				numName += four
			if num[actual_index] == "5":
				numName += five
			if num[actual_index] == "6":
				numName += six
			if num[actual_index] == "7":
				numName += seven
			if num[actual_index] == "8":
				numName += eight
			if num[actual_index] == "9":
				numName += nine
			if num[actual_index] != "0":				
				numName += hundred
				if num[actual_index:len(num)].count("0") != len(num)-actual_index-1:
					numName += "and "
		if actual_index == ten2:
			if num[actual_index:actual_index+2] ==  "10":
				numName += ten
			if num[actual_index:actual_index+2] ==  "11":
				numName += eleven
			if num[actual_index:actual_index+2] == "12":
				numName += twelve 
			if num[actual_index:actual_index+2] == "13":
				numName += thirteen
			if num[actual_index:actual_index+2] == "14":
				numName += fourteen
			if num[actual_index:actual_index+2] == "15":
				numName += fifteen 
			if num[actual_index:actual_index+2] == "16":
				numName += sixteen 
			if num[actual_index:actual_index+2] == "17":
				numName += seventeen 
			if num[actual_index:actual_index+2] == "18":
				numName += eighteen
			if num[actual_index:actual_index+2] == "19":
				numName += nineteen
			if num[actual_index] == "2":
				numName += twenty
			if num[actual_index] == "3":
				numName += thirty
			if num[actual_index] == "4":
				numName += fourty
			if num[actual_index] == "5":
				numName += fifty
			if num[actual_index] == "6":
				numName += sixty
			if num[actual_index] == "7":
				numName += seventy
			if num[actual_index] == "8":
				numName += eighty
			if num[actual_index] == "9":
				numName += ninety
		if actual_index == one2 and actual_index -1 >= 0 and num[actual_index-1] != "1":
			if num[actual_index] == "1":
				numName += one
			if num[actual_index] == "2":
				numName += two
			if num[actual_index] == "3":
				numName += three
			if num[actual_index] == "4":
				numName += four 
			if num[actual_index] == "5":
				numName += five
			if num[actual_index] == "6":
				numName += six 
			if num[actual_index] == "7":
				numName += seven 
			if num[actual_index] == "8":
				numName += eight
			if num[actual_index] == "9":
				numName += nine
			if actual_index == one2 and (num[actual_index] != "0" or num[actual_index-1] != "0" or num[actual_index-2] != "0"):
				numName += million
				print actual_index, " : ", num[actual_index],num[actual_index-1],num[actual_index-2]
		# Thousands
		if actual_index == hund1:
			if num[actual_index] == "1":
				numName += one
			if num[actual_index] == "2":
				numName += two
			if num[actual_index] == "3":
				numName += three
			if num[actual_index] == "4":
				numName += four
			if num[actual_index] == "5":
				numName += five
			if num[actual_index] == "6":
				numName += six
			if num[actual_index] == "7":
				numName += seven
			if num[actual_index] == "8":
				numName += eight
			if num[actual_index] == "9":
				numName += nine
			if num[actual_index] != "0":
				numName += hundred
				if num[actual_index:len(num)].count("0") != len(num)-actual_index-1:
					numName += "and "
		if actual_index == ten1:
			if num[actual_index:actual_index+2] ==  "10":
				numName += ten
			if num[actual_index:actual_index+2] ==  "11":
				numName += eleven
			if num[actual_index:actual_index+2] == "12":
				numName += twelve
			if num[actual_index:actual_index+2] == "13":
				numName += thirteen
			if num[actual_index:actual_index+2] == "14":
				numName += fourteen
			if num[actual_index:actual_index+2] == "15":
				numName += fifteen
			if num[actual_index:actual_index+2] == "16":
				numName += sixteen
			if num[actual_index:actual_index+2] == "17":
				numName += seventeen
			if num[actual_index:actual_index+2] == "18":
				numName += eighteen
			if num[actual_index:actual_index+2] == "19":
				numName += nineteen

			if num[actual_index] == "2":
				numName += twenty
			if num[actual_index] == "3":
				numName += thirty
			if num[actual_index] == "4":
				numName += fourty
			if num[actual_index] == "5":
				numName += fifty
			if num[actual_index] == "6":
				numName += sixty
			if num[actual_index] == "7":
				numName += seventy
			if num[actual_index] == "8":
				numName += eighty
			if num[actual_index] == "9":
				numName += ninety
		if actual_index == one1 and num[actual_index-1] != "1":
			if num[actual_index] == "1":
				numName += one
			if num[actual_index] == "2":
				numName += two
			if num[actual_index] == "3":
				numName += three
			if num[actual_index] == "4":
				numName += four
			if num[actual_index] == "5":
				numName += five
			if num[actual_index] == "6":
				numName += six
			if num[actual_index] == "7":
				numName += seven
			if num[actual_index] == "8":
				numName += eight
			if num[actual_index] == "9":
				numName += nine
			if num[actual_index] != "0" or num[actual_index-1] != "0" or num[actual_index-2] != "0":
				numName += thousand
		#Hundreds
		if actual_index == hund:
			if num[actual_index] == "1":
				numName += one
			if num[actual_index] == "2":
				numName += two
			if num[actual_index] == "3":
				numName += three
			if num[actual_index] == "4":
				numName += four
			if num[actual_index] == "5":
				numName += five
			if num[actual_index] == "6":
				numName += six
			if num[actual_index] == "7":
				numName += seven
			if num[actual_index] == "8":
				numName += eight
			if num[actual_index] == "9":
				numName += nine
			if num[actual_index] != "0":
				numName += hundred 
				if num[actual_index:len(num)].count("0") != len(num)-actual_index-1:
					numName += "and "
		if actual_index == tens:
			if num[actual_index:actual_index+2] ==  "10":
				numName += ten
			if num[actual_index:actual_index+2] ==  "11":
				numName += eleven
			if num[actual_index:actual_index+2] == "12":
				numName += twelve
			if num[actual_index:actual_index+2] == "13":
				numName += thirteen
			if num[actual_index:actual_index+2] == "14":
				numName += fourteen
			if num[actual_index:actual_index+2] == "15":
				numName += fifteen
			if num[actual_index:actual_index+2] == "16":
				numName += sixteen
			if num[actual_index:actual_index+2] == "17":
				numName += seventeen
			if num[actual_index:actual_index+2] == "18":
				numName += eighteen
			if num[actual_index:actual_index+2] == "19":
				numName += nineteen
			if num[actual_index] == "2":
				numName += twenty
			if num[actual_index] == "3":
				numName += thirty
			if num[actual_index] == "4":
				numName += fourty
			if num[actual_index] == "5":
				numName += fifty
			if num[actual_index] == "6":
				numName += sixty
			if num[actual_index] == "7":
				numName += seventy
			if num[actual_index] == "8":
				numName += eighty
			if num[actual_index] == "9":
				numName += ninety
		if actual_index == ones and num[actual_index-1] != "1":
			if num[actual_index] == "1":
				numName += one
			if num[actual_index] == "2":
				numName += two
			if num[actual_index] == "3":
				numName += three
			if num[actual_index] == "4":
				numName += four
			if num[actual_index] == "5":
				numName += five
			if num[actual_index] == "6":
				numName += six
			if num[actual_index] == "7":
				numName += seven
			if num[actual_index] == "8":
				numName += eight
			if num[actual_index] == "9":
				numName += nine
		actual_index += 1
	return numName[0:len(numName)-1]

def lenNameNumTo(num):
	summ = 0
	for a in range(1,num+1):
		print numToWords(a)
		summ += len(numToWords(a).replace(" ","").replace("-",""))
	return summ
