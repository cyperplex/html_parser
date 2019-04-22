# Author : Owen Corcoran
# Test Web page element scraper

import json
import re
import requests

from bs4 import BeautifulSoup


def site_reader(url, download_element):
	response = requests.get(url)
	if response.status_code == 200:
		try:
			response = requests.get(url)
			soup = BeautifulSoup(response.text, 'html.parser')
			img_tags = soup.find_all('img')
			urls = [img['src'] for img in img_tags]
			
			for url in urls:
				filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
				with open(filename.group(1), 'wb') as f:
					if 'http' not in url or 'https' not in url:
						url = '{}{}'.format(site, url)
						response = requests.get(url)
						f.write(response.content)
					else:
						print("Unable to connect to specified site return code !=200")


# Obtain configuration settings
def import_config(configname):
	'''
	This function will read in and set the global config options for the program
	:param configname: Name of the JSON config file to load
	:return:
	'''
	# Global variable definitions, variables/contents available to all scopes
	global url
	global download_element
	global outputdir
	try:
		with open(configname) as f:
			data = json.loads(f.read())
			url = (data[0]['url'])
			download_element = (data[0]['download_element'])
			outputdir = (data[0]['output'])
		# Call site parser function
		site_reader(url, download_element)
	except ValueError:
		print('Error with value read from configfile')


if __name__ == "__main__":
	import_config('config.json')
