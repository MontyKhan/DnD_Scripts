from random import randrange as rand	# For rolling of dice
import sys				# For taking initial arguments

class Node:
	def __init__(self,name,init,cr,hp,ac,speed,stats,traits,weapons,spells,abilities):
		self.name = name
		self.init = init
		self.cr = cr
		self.hp = hp
		self.ac = ac
		self.speed = speed
		self.stats = stats
		self.traits = traits
		self.weapons = weapons
		self.spells = spells
		self.abilities = abilities
		self.next = None

	def __repr__(self):
		val = self.name + " Init: " + str(self.init) + " CR: " + self.cr
		val += " HP: " + self.hp + " AC: " + self.ac + " Speed: " + self.speed + "\n\n"
		val += "STR\tDEX\tCON\tINT\tWIS\tCHA\n"
		val += self.stats.replace(";","\t") + "\n"
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
		while node is not None:
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
file = open(sys.argv[1], "r")

file_contents = file.readlines()

file_contents.pop(0)

# Declare variables
initiative_table = LinkedList()

# Add contents to list
for line in file_contents:
	line = line.replace('\n', '')
	line = line.replace('endl','\n')
	line = line.replace('n/a','')
	line = line.split(',')
	initiative = rand(1,21,1) + int(line[1])
	# entry = Node(line[0],initiative)
	entry = Node(line[0],initiative,line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10])
	
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

print initiative_table

node = initiative_table.head

while node.next is not None:
	node = node.next

node.next = initiative_table.head

val = "\n"

while (val is not "x"):
	node = node.next
	print node
	input = raw_input()

	# Remove inputted line
	print ("\033[A                             \033[A")

	input = input.replace('\n', '')
	arguments = input.split(' ')

	if (arguments[0] == "cont"):
		continue
	elif (arguments[0] == "add"):
		entry = Node(arguments[1],int(arguments[2]),'Player','','','','','','','','')
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
	elif (arguments[0] == "rm"):
		tmp = node
		while (node.name != arguments[1]):
			node = node.next

		initiative_table.remove(node)
		
		node = tmp
	elif (arguments[0] == "get"):
		print initiative_table.get(arguments[1])
		raw_input()
	elif (arguments[0] == "exit"):
		print("Exiting...\n")
		break
