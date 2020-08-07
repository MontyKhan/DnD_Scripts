import xml.etree.ElementTree as et

def import_monster(arguments):
	if (len(arguments) == 1):
		print ("Insufficient arguments!\n")
		return None

	tree = et.parse("stats/monster_manual.xml")
	root = tree.getroot()

	if (root.tag != "mm"):
		print ("Monster manual not found!\n")
		return None

	# Iterate through entries in monster manual
	for monster in root:
		for child in monster:
			if (child.tag == "name" and child.text == arguments[1]):
				print ("Found!")
				return monster
			else:
				continue

	print ("Not found!")
