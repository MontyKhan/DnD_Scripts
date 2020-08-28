# DnD Scripts

A collection of Python scripts to aid with DMing in DnD. Developed on Ubuntu 18.04.

## Files:

* **main.py** - Main command loop. Contains functions for commands detailled below.
* **monster_manual.py** - Contains functions for accessing monster_manual.xml
* **create_encounter.py** - Contains functions for creating an .xml file describing an encounter. Under development.

  
## Commands: 
  * *add (name) (initiative)* - Adds player character with that name, and inserts them into the initiative order at the right place.
  * *get (name)* - Prints details of character in initiative order with that name.
  * *import (name) (init)* - Imports matching character from monster_manual.xml with init as their initiative.
  * *import (name)* - Imports matching character from monster_manual.xml with random init.
  * *loadxml (path)* - Load encounter from .xml file at path.
  * *rm (name)* - Remove character in initiative order with matching name.
  * *printall* - Print all character names in initiative order.
  * *next* - Proceeds to next character in initiative order.
  * *exit* - Exits the program.
