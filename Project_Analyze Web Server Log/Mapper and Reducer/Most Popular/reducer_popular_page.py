#!/usr/bin/python

# Loop around the data
# It will be in the format key\tval
# where key is the request line from the client, val is the status code.
#
# We will find the most popular file's pathname and number of
# occurrences.

import sys

oldKey = None
count = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    request, status = data_mapped
    
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", count
        oldKey = thisKey;
        count = 0

    oldKey = thisKey
    count += 1

if oldKey != None:
    print oldKey, "\t", count
