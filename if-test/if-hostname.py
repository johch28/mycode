#!/usr/bin/env python3
hostname = input('What is your Hostname:')
if hostname == 'MTG' or hostname == 'mtg' or hostname == 'mTg' or hostname == 'MTg' or hostname == 'MtG' or hostname == 'mTG':
	print('The hostname was found to be mtg')
	print('host name matches expected config')
	
if hostname != 'MTG' or 'mtg' or 'mTg' or 'MTg' or 'MtG' or 'mTG':
	print('Error')
	print('exiting the script') #leaving script
