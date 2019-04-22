# This module will read the application configuration file and return each value for each config option defined
# Owen Corcoran
import xml.etree.ElementTree as ET

def config_reader(inputconfig):
	"""Traverse the given XML element tree to convert it into a dictionary.
    :param element_tree: An XML element tree
    :type element_tree: xml.etree.ElementTree
    :rtype: dict
    """
	tree = ET.parse(inputconfig)
	root = tree.getroot()
	if inputconfig is None:
		print("Error - Cannot read config file.")
	else:
		for element in root.iter('item'):
			print("--------Loading Config Element--------")
			print(element.attrib)

if __name__ == "__main__":
	config_reader('config.xml')
