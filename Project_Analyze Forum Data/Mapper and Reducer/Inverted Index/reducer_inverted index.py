#!/usr/bin/python

import sys
import re

# Loop around the data
# It will be in the format key\tval

count = 0
list_ID = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisID, thisBody = data_mapped

    regex = r'\b(fantastic)\b'
    if re.search(regex, thisBody, re.IGNORECASE):
        count += 1
    regex = r'\b(fantastically)\b'
    if re.search(regex, thisBody, re.IGNORECASE):
        list_ID.append(thisID)

print "Count of word 'fantastic'", "\t", count

list_ID.sort()

print "List of ID contained work 'fantastically'", "\t", list_ID