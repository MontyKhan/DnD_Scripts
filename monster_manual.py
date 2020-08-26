import xml.etree.ElementTree as et

def import_monster(name):
	tree = et.parse("stats/monster_manual.xml")
	root = tree.getroot()

	if (root.tag != "mm"):
		print ("Monster manual not found!\n")
		return None

	# Iterate through entries in monster manual
	for monster in root:
		for child in monster:
			if (child.tag == "name" and child.text == name):
				print ("Found!")
				return monster
			else:
				continue

	print ("Not found!")
	return None
