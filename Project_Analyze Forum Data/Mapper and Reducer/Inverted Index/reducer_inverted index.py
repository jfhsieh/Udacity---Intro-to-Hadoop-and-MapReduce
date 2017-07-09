#!/usr/bin/python

import sys

# Loop around the data
# It will be in the format key\tval

count = 0
list_ID = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    
    thisID, thisBody = data_mapped

    if thisBody == "fantastic":
        count += 1
    if thisBody == "fantastically":
        list_ID.append(thisID)

print "Count of word 'fantastic'", "\t", count
print "List of ID contained work 'fantastically'", "\t", list_ID