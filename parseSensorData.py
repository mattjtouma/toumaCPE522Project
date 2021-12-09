""" here is 
a multi-line
comment
"""

import sys
import csv

# file name is provided as a command-line argument
infile = open(sys.argv[1])
reader = csv.reader(infile)

# Empty lists
headings = []
rows = []

# Note that min, max and sum are python keywords.
# Don't use them as variables.

maxTemp = 0
minTemp = 99
averageTemp = 0

# Algorithm:
# Read the next line
headings = reader.next()
#print "Headings are: ", headings

for line in reader:
    #print "line: ", line
    rows.append(float(line[1]))
    if float(line[1]) > maxTemp:
        maxTemp = float(line[1])
    if float(line[1]) < minTemp:
        minTemp = float(line[1])

Total = sum(rows)
averageTemp = Total/len(rows)

print "Temperature Report"
print "Average: ", averageTemp
print "Maximum: ", maxTemp
print "Min: ", minTemp


