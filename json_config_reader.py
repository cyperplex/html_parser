# This module will read the application configuration file and return each value for each config option defined
# Owen Corcoran

import json

def import_config(configname):
	'''
	This function will read in and set the global config options for the program
	:param configname: Name of the JSON config file to load
	:return:
	'''
	
	global url
	global download_element
	global outputdir
	
	try:
		with open(configname) as f:
			data = json.loads(f.read())
			url = (data[0]['url'])
			download_element = (data[0]['download_element'])
			outputdir = (data[0]['output'])
	except ValueError:
         print('Error with value read from configfile')

if __name__ == "__main__":
	import_config('config.json')

