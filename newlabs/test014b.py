#!/usr/bin/env python3

# Import the operating system module 
import os

# Open the output file for writing
in_file =  open('hamlet.txt', 'r')

# Count the number of lines in the file
line_count = 0

#############################################################
#Loop through each line in input file. . . print out the file
#############################################################
for a_line in in_file:
	print(a_line, end='')			# using the end parameter, extra line feeds not added
	line_count +=1				# This is the same as line_count = Line_count +1

####################################################################
#IMPORTANT DO NOT FORGET TO CLOSE THE FILE
###############################################################

in_file.close()

print()

print("The numbers of lines contained in this file were: ", line_count)
print()

#####################################################################
# This is just demonstrating another way to increment a count variable
#... Other languages typiocally do something line "i = i + 1"
#tmp_lc is a temporary line count
####################################################################
tmp_lc = line_count
tmp_lc = tmp_lc + 1		#this is the typiocal way other programming languages increment
print("The value of variable tmp_lc: ", tmp_lc)
