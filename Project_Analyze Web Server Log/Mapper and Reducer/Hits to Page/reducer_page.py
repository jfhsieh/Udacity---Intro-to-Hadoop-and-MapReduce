#!/usr/bin/python

# Loop around the data
# It will be in the format key\tval
# where key is the request line from the client, val is the status code.
#
# The number of hits to the page "/assets/js/the-associates.js" 
# will be calculated.

import sys

count = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    request, status = data_mapped
    
    if (request.find("/assets/js/the-associates.js") >= 0):
    	count += 1

print "Total hits", "\t", count

