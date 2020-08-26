from cmd import Cmd
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

class MainPrompt(Cmd):
	def do_exit(self,inp):
		return True

	def do_loadxml(self,inp):
		tree = et.parse(inp)
		root = tree.getroot()

		if (root.tag != "encounter"):
			print("Incorrect format. Not an encounter!\n")
			return False

		self.initiative_table = LinkedList()

		for monster in root:
			init_field = monster.find("init")
			init_field.text = str(rand(1,21,1) + int(init_field.text))
			entry = Node(monster)

			if self.initiative_table.head is None:
				self.initiative_table.head = entry
				continue

			node = self.initiative_table.head

			if (entry.init >= self.initiative_table.head.init):
				self.initiative_table.change_head(entry)
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

		print (self.initiative_table)
		print ("\n")

		node = self.initiative_table.head
	
		while node.next is not None:
			node = node.next

		node.next = self.initiative_table.head
		self.active_node = node

	def do_next(self, inp):
		self.active_node = self.active_node.next
		print (self.active_node)
		return False



# Main loop
MainPrompt().cmdloop()
