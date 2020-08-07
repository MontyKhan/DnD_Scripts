import monster_manual as mm
import xml.etree.ElementTree as et
from random import randrange as rand	# For rolling of dice
import sys				# For taking initial arguments

class Node:
	def __init__(self,entry):
		self.wipe_all()
		for child in entry:
			if (child.tag == "name"):
				self.name = child.text
			elif (child.tag == "init"):
				self.init = int(child.text)
			elif (child.tag == "cr"):
				self.cr = child.text
			elif (child.tag == "hp"):
				self.hp = child.text
			elif (child.tag == "ac"):
				self.ac = child.text
			elif (child.tag == "speed"):
				self.speed = child.text
			elif (child.tag == "stats"):
				self.stats = child.text
			elif (child.tag == "traits"):
				self.traits = child.text
			elif (child.tag == "weapons"):
				self.weapons = child.text
			elif (child.tag == "spells"):
				self.spells = child.text
			elif (child.tag == "abilities"):
				self.abilities = child.text

	def wipe_all(self):
		self.name = ""
		self.init = "0"
		self.cr = "0"
		self.hp = "0"
		self.ac = "0"
		self.speed = "0"
		self.stats = "0;0;0;0;0;0"
		self.traits = ""
		self.weapons = ""
		self.spells = ""
		self.abilities = ""
		self.next = None

	def __repr__(self):
		val = self.name + " Init: " + str(self.init) + " CR: " + self.cr
		val += " HP: " + self.hp + " AC: " + self.ac + " Speed: " + self.speed + "\n\n"
		val += "STR\tDEX\tCON\tINT\tWIS\tCHA\n"
		val += self.stats.replace(";","\t") + "\n\n"
		val += self.traits + "\n\n"
		val += self.weapons + "\n"
		val += self.spells + "\n"
		val += self.abilities + "\n"
		return val

	def insert_after(self, entry):
		if (self.next is not None):
			tmp = self.next
			entry.next = tmp
			self.next = entry
		else:
			self.next = entry

	def insert_before(self, entry):
		tmp = self
		self.name = entry.name
		self.init = entry.init
		self.insert_after(tmp)

class LinkedList:
	def __init__(self):
		self.head = None

	def __repr__(self):
		node = self.head
		nodes = []
		nodes.append(node.name + " " + str(node.init))
		node = node.next
		while (node is not None and node is not self.head):
			nodes.append(node.name + " " + str(node.init))
			node = node.next
		nodes.append("None")
		return " -> ".join(nodes)

	def change_head(self, new_head):
		new_head.next = self.head
		self.head = new_head

	def get_last(self):
		node = self.head
		while (node.next != None or node.next != self.head):
			node = node.next
		return node

	def remove(self,target):
		node = self.head
		while (node.next != target):
			node = node.next
		node.next = node.next.next

	def get(self,target_name):
		node = self.head
		while (node.name != target_name):
			node = node.next
		return node


# Main function starts here.
tree = et.parse(sys.argv[1])
root = tree.getroot()

if (root.tag != "encounter"):
	print("Incorrect format. Not an encounter!\n")
	exit()

# Declare variables
initiative_table = LinkedList()

for monster in root:
	init_field = monster.find("init")
	init_field.text = str(rand(1,21,1) + int(init_field.text))
	entry = Node(monster)

	if initiative_table.head is None:
		initiative_table.head = entry
		continue

	node = initiative_table.head

	if (entry.init >= initiative_table.head.init):
		initiative_table.change_head(entry)
		continue

	while node is not None:
		if (node.next is None):
			node.insert_after(entry)
			break
		elif (entry.init > node.next.init):
			node.insert_after(entry)
			break
		else:
			node = node.next

print (initiative_table)
print ("\n")

node = initiative_table.head

while node.next is not None:
	node = node.next

node.next = initiative_table.head

val = "\n"

while (val != "x"):
	node = node.next
	print (node)
	input = raw_input()

	# Remove inputted line
	print ("\033[A                             \033[A")

	input = input.replace('\n', '')
	arguments = input.split(' ')

	if (arguments[0] == "cont"):
		continue
	elif (arguments[0] == "add"):
		player = et.Element('player')

		player_name = et.Element('name')
		player_name.text = arguments[1]
		player.append(player_name)

		player_init = et.Element('init')
		player_init.text = arguments[2]
		player.append(player_init)

		entry = Node(player)
		tmp = node
		if (initiative_table.head.init < entry.init):
			while (node.next != initiative_table.head):
				node = node.next
			node.next = None
			initiative_table.change_head(entry)
			while (node.next != None):
				node = node.next
			node.next = initiative_table.head
		else:
			while not ((entry.init < node.init) and (entry.init > node.next.init)):
				if (entry.init < node.init) and (node.next == initiative_table.head):
					break
				node = node.next

			node.insert_after(entry)
		node = tmp
		print ("Press ENTER to continue...")
		raw_input()
	elif (arguments[0] == "rm"):
		tmp = node
		while (node.name != arguments[1]):
			node = node.next

		initiative_table.remove(node)

		node = tmp
		print ("Press ENTER to continue...")
		raw_input()
	elif (arguments[0] == "get"):
		print (initiative_table.get(arguments[1]))
		print ("Press ENTER to continue...")
		raw_input()
	elif (arguments[0] == "import"):
		new_monster = mm.import_monster(arguments)

		init_field = new_monster.find("init")
		if (len(arguments) == 3):
			init_field.text = arguments[2]
		else:
			init_field.text = str(rand(1,21,1) + int(init_field.text))

		entry = Node(new_monster)
		tmp = node
		if (initiative_table.head.init < entry.init):
			while (node.next != initiative_table.head):
				node = node.next
			node.next = None
			initiative_table.change_head(entry)
			while (node.next != None):
				node = node.next
			node.next = initiative_table.head
		else:
			while not ((entry.init < node.init) and (entry.init > node.next.init)):
				if (entry.init < node.init) and (node.next == initiative_table.head):
					break
				node = node.next

			node.insert_after(entry)
			node = tmp
		print ("Press ENTER to continue...")
		raw_input()
	elif (arguments[0] == "printall"):
		print ("test")
		print (initiative_table)
		print ("Press ENTER to continue...")
		raw_input()
	elif (arguments[0] == "exit"):
		print("Exiting...\n")
		break
