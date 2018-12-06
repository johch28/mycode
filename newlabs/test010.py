#!/usr/bin/env python3
# a_list is the original list
a_list = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g']

######################################################
#  Print out a subset of the list. Start with index 3, go to the end of the list. 
# This prints out the list of [ 'd', 'e', 'f', 'g']
################
# This is slicing the list
###############################################################
print(a_list[2:5])
print(". . . CHECKING did it return . . . ['d', 'e', 'f', 'g']")
print()

###################################################################
# Print out the LAST item in the list,
# NOTE: -1 means the last item in the list

#######################################################################
print(a_list[-1])
print(". . . CHECKING did it return g")
print()

######################################################################
print(a_list[:5])
print(". . . CHECKING did it return . . . ['a', 'b', 'c', 'd']")
print()
