#!/usr/bin/env python3

#Initialize Two Set objects, using curly brackets, this important for script
chicago_zoo_set = {'Kangaroo', 'Leopard', 'Moose', 'Polar Bear', 'Bobcat'}
sandiego_zoo_set = {'Kangaroo', 'Lion', 'Grizzly Bear', 'Wildcat', 'Antelope'}

print()
print("SET OBJECTS . . .")
print('Chicago Zoo: ', chicago_zoo_set)
print('San Diego Zoo: ', sandiego_zoo_set)
print()

print("Common animals to both the Chicago and San Diego Zoo: ")
print("Intersection of Chicago and San Diego Zoo")
print(chicago_zoo_set.intersection(sandiego_zoo_set))
# Only Kangaroo, this will list the only item that is in both sets

print()
print("Unique animals at the Chicago Zoo: ")
print("These are items at the Chicago Zoo, but NOT at the San Diego Zoo")
print(chicago_zoo_set.difference(sandiego_zoo_set))
# Should include Leopard, Moose, Polar Bear, and Bobcat
# NOTE: It might be printed in a different order

print()
print("Unique animals at the San Diego Zoo: ")
print("These are items at the San Diego Zoo, but NOT at the Chicago Zoo")
print(sandiego_zoo_set.difference(chicago_zoo_set))

print()

# Should include Lion, Grizzly Bear, Wildcat, Antelope
# NOTE: It might be printed in a different order



