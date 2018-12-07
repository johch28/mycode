#!/usr/bin/env python3
my_list = [ "192.168.0.5", 5060, "UP" ]
my_list2 = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#COMMENTS NONE
print()
print("The first item in the list (IP): " + my_list[0] )
#[0] represents the first item in the list, lists always stay with 0

print("The second item in the list (port): " + str(my_list[1]) )
# [1] is the second item, str indicates that the integer has to be read as a string

print("The last item in the list (state): " + my_list[2] )
# [3] corresponds to the word UP

print()

print("When I attempt to connect to " +str(my_list2[4:6]))
print("I am unable to ping ports " +str(my_list2[0:3]))

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print()

### Tuple will import information from elsewhere, Tuples will be static and they can pull from ither elements that can be modified##