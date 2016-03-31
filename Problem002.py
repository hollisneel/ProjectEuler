###############
# Each new term in the Fibonacci sequence is generated by adding the 
# previous two terms. By starting with 1 and 2, the first 10 terms 
# will be:
#
#    1,2,3,5,8,13,21,34,55,89
#
# By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued terms.
###############

fibonacciSequence = [1,2]
number = 0
count = 0
sum = 2
while number < 4000000:
	number = fibonacciSequence[count] + fibonacciSequence[count+1]
	fibonacciSequence.append(number)
	count += 1
	if number %2 == 0:
		sum += number
print sum