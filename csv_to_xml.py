import sys

# Set path to input file as first argument
filepath = sys.argv[1]

# Open file, and load contents to array
file = open(filepath,"r")
file_contents = file.readlines()
header = file_contents[0]
header = header.lower()
header = header.split(",")

# Write output to file with same name but different format
output_path = filepath.replace(".csv",".xml")
output = open(output_path, "w")

# Remove headers from input file
file_contents.pop(0)

output.write("<encounter>\n")

# Iterate through file
for line in file_contents:
	line = line.replace('\n', '')
	line = line.replace('endl','\n')
	#line = line.replace('n/a','')
	monster = line.split(',')

	# Write encapsulating tag (indent 1)
	output.write("\t<monster>\n")

	length = len(header)
	for i in range(length):
		if (monster[i] != "n/a"):
			output.write("\t\t<")
			output.write(header[i])
			output.write(">")
			output.write(monster[i])
			output.write("</")
			output.write(header[i])
			output.write(">\n")
	
	output.write("\t</monster>\n\n")

output.write("</encounter>")
	
