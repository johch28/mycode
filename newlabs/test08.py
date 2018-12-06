#!/usr/bin/env python3

##################################################
# cels_list is the LIST of Celcius temperatures
# fahr_list is the LIST of fahrenheit Temps

##################################################
cels_list = [-2, 0, 5, 10, 15, 25, 32, 38, 40]
fahr_list = [] #Empty list

###################################################
#Use a FOR loop to access each item in the list
# Find the corresponding fahrneheit temp
# Append it to the fahr_list
###################################################
for c in cels_list: 
	f_temp = c * 1.8 + 32.0
	fahr_list.append(f_temp)

print("The Celsius list: ", cels_list)
print("The farenheit list: ", fahr_list)
