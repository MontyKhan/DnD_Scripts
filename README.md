# DnD Scripts

A collection of Python scripts to aid with DMing in DnD. Developed on Ubuntu 18.04.

## Scripts:

initiative_counter.py - Loads combatants from file and rolls initiative for them. Human players can then be added.
  Arguments: Path to file.
  Commands: add (name) (initiative)   Adds player character with that name, and inserts them into the initiative order at the right place.
            get (name)                Prints details of character in initiative order with that name.
            cont                      Proceeds to next character in initiative order. Can also be achieved by entering a blank line.
            exit                      Exits the program.
