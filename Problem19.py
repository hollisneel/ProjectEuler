###############################
#
# Project Euler Problem 19
#
###############################

# months
# January:31
# February:28-29
# March: 31
# April: 30
# May: 31
# June: 30
# July: 31
# August: 31
# September: 30
# October: 31
# November: 30
# December: 31

num_days = 0
first_of_months = {}
for a in range(1,101):
	if a%4 == 0:
		first_of_months[a] = [num_days+1,num_days+32,num_days+61,num_days+92,num_days+122,num_days+153,num_days+183,num_days+214,num_days+245,num_days+275,num_days+306,num_days+336]
		num_days += 366
	else:
		first_of_months[a] = [num_days+1,num_days+32,num_days+60,num_days+92,num_days+122,num_days+153,num_days+183,num_days+214,num_days+245,num_days+275,num_days+306,num_days+336]
		num_days += 365
keys = first_of_months.keys()
num_sundays = 0
for a in range(len(keys)):
	for b in range(len(first_of_months[keys[a]])):
		if first_of_months[keys[a]][b]%7 == 6:
			num_sundays+= 1

