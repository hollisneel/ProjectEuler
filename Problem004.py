####################
# A palindromic number reads the same both ways. The largest
# plindrome made from the product of two 2-digit numbers is 
# 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 
# 3-digit numbers.
#
####################
palindrome = []
def isPalindrome(num):
	string = str(num)
	value = 0
	for x in range(len(string)):
		if string[x] == string[len(string) - 1 -x]:
			value += 1
	if value == len(string):
		return 1
	else:
		return 0

for x in range(999):
	for y in range(999):
		if isPalindrome((999 - x)*(999-y)):
			palindrome.append((999-x)*(999-y))
palindrome.sort()
print palindrome[len(palindrome)-1]
