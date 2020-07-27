from random import randrange as rand
import keyboard

class Node:
	def __init__(self,name,init):
		self.name = name
		self.init = init
		self.next = None

	def __repr__(self):
		val = self.name + " " + str(self.init)
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
	

file = open("./stats/encounter1.csv", "r")

file_contents = file.readlines()

file_contents.pop(0)

# Declare variables
initiative_table = LinkedList()

# Add contents to list
for line in file_contents:
	line = line.replace('\n', '')
	line = line.split(',')
	initiative = rand(1,21,1) + int(line[4])
	entry = Node(line[0],initiative)
	
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
	print node
	node = node.next
	#val = keyboard.read_key()
	val = raw_input()
	print ("\033[A                             \033[A")
