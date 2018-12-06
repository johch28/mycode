#!/usr/bin/env python3

#FLOATS FORMATTING

my_num = 1234.56789
my_pi = 3.1415926535

print("My number is: ", my_num)
print("The value of pi: ", my_pi)
print()

###################################################################
# Format to 2 decimal places
# NOTE that you dont need the 0 before the .2f

#######################################################################
print(format(my_num, '0.2f'), "Print using 2 decimal places")
print(format(my_num, '.2f'), "Also print using 2 decimal places")
print("NOTE that it rounded my result! ! !")
print()

#Format to only 1 decimal place
print(format(my_num, '.1f'), "Also prints using 1 decimal places")
print("Note that is rounded my result ! ! !")

#Format PI from 10 decimal places to 6 decimal places
print(format(my_num, '.9f'), "Also prints using 6 decimal places")
print("NOTE that it rounded my result! ! !")