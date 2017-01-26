#author : Joseph Appeah
import os

a = open("AVGdata.csv","a+")
records = []

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
	if ("_AVGDATA_" in f):
		print f
		with open(f) as file:
			for line in file:
				line = line[1:-1]
				print line
				records = line.split("--")
for record in records:
	print record
	a.write(record + "\n")
