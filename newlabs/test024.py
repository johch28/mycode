#!/usr/bin/env python3

# Initializating a dictionary of phone numbers /  names
# Here the persons name is a key
phone_dict = {
	'Chris Johnson': ['3136954330', 'MI'],
	'BUDA': ['8174563622', 'TX'],
	'FM 98 WJLB': ['3132987098', 'MI'],
	'VZW NRB': ['8668998998', 'TX'],
}


print()
print(" The phone dictionary. . . ")
print(phone_dict)

#########################################################
# Access one individual item in the dictionary
# NOTE that user_name is used as the key to look in the dictionary
#########################################################
user_name = "BUDA"
print("The phone number for ", user_name, "is", phone_dict[user_name][0])
print(" The state for ", user_name, "is", phone_dict[user_name][1])
print()


#########################################################
#Ask the user for a persons name
#########################################################
input_name = input("Please enter a person's name:")
print("The phone number for", input_name, "is", phone_dict[input_name][0])
print()

#########################################################
#Access one individual item in the dictionary
#NOTE that you can select meaningful names to describe your key value pairs
#########################################################
#for full_name, phone_info in phone_dict.items():
#	print("The phone number for", full_name, "is", phone_info[0])
#	print("The phone location is ", phone_info[1])
#	print()




