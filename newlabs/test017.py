#!/usr/bin/env python3

########################################################################
#STRING SPLITTING
#####################################

# Input string that use different chracters as delimiters
s1 = "Chris,Jene,Johnson"
s2 = "Donald Victoria Andrew Sarah"
s3 = "Donald@Victoria@Andrew@Sarah"

# PRINT OUT THE INITIAL STRINGS
print("s1:", s1)
print("s2:", s2)
print("s3:", s3)

# Split the string create a list using a comma like seperator
list1 = s1.split(',')
print("list1: ", list1)

# Split the string create a list using the default space
list2 = s2.split()
print("list2: ", list2)

# Split the string create a list using the @ character as a delimiter
list3 = s3.split('@')
print("list3: ", list3)

