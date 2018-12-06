#!/usr/bin/env python3

##################################################################
# Calculating Fibonacci numbers
# This is a famous mathematical series.

# 1 1 2 3 5 8 13 21 34

# The first two numbers in the series are 1
# The third number is assigned the sum of the previous two numbers.
#####################################################################


#####################################################################
# The traditional way to program the Fibonacci series
####################################################################
def trad_fib(n):
	a = 1		# The first number in the series
	b = 1		# The second number in the series

	while b < n:
		print(a, end=" ")
		old_b = b
		b = a + b
		a = old_b
	print(a, end=" ")
	print()
	return a

x = trad_fib(400)
print("The Fibonacci numbers that is less than 400. . .", x)
# This will present numbers under 400

print()

x = trad_fib(2000)
print("The Fibonacci numbers that is less than 2000. . .", x)
#This will present numbers under 2000

print()

print(" Chris is fancy ")

print()
	