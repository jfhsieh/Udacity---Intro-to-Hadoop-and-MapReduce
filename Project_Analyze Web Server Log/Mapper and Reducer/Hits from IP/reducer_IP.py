#!/usr/bin/python

# Loop around the data
# It will be in the format key\tval
# where key is the IP from the client, val is the status code.
#
# The number of hits from IP 10.99.99.186 will be calculated.

import sys

count = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    ip, status = data_mapped
    
    if (ip == "10.99.99.186"):
    	count += 1

print "Total hits", "\t", count

