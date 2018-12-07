#!/usr/bin/env python3

##################################################################
# Calculating Fibonacci numbers
# This is a famous mathematical series.

# 1 1 2 3 5 8 13 21 34

# The first two numbers in the series are 1
# The third number is assigned the sum of the previous two numbers.
#####################################################################
# Note that the function returns the value of a 
# This is the last number displayed, as "new a value = b"
#
# If changed to b, then it displays the "new b value, a + b"
#####################################################################

####################################################################
def fib(n):
	a, b = 0, 1		
	while b < n:
		print(b, end=" ")
		a, b = b, a+b		#See the meaning below

	print()			#Space

	return a		#return the last number displayed

######################################################
#Meaning of a, b -  b, a+b

#This does multople assignements ans uses original values!

#examine the left side of the awssignment operartotr "="
#The variables a and b will both be given new values

#a will be assigned to the old value of b
#b will be assigned to the sumn of the old values of a+b
###############################################################

# Call the function to display the Fibonacci numbers less than 100
x = fib(100)
print("The Fibonacci number that is less than 100. . .", x)
# This will present numbers under 100

print()

#Call the function, to display the Fibonacci numbers less than 500
x = fib(500)
print("The Fibonacci number that is less than 500. . .", x)
#This will present numbers under 500
print()

#Call the function, to display the Fibonacci numbers less than 2000
x = fib(2000)
print("The Fibonacci numbers that is less than 2000. . .", x)
#This will present numbers under 2000

print()

print(" Chris is fancy ")

print()




	