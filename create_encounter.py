import monster_manual as mm
import xml.etree.ElementTree as et
import sys


root = et.Element("encounter")
monster = mm.import_monster(sys.argv)

root.append(monster)

output = "stats/new_enctr.xml"
tree = et.ElementTree(root)
tree.write(output)
