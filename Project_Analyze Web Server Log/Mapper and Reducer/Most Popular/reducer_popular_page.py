#!/usr/bin/python

# Loop around the data
# It will be in the format key\tval
# where key is the request line from the client, val is the status code.
#
# We will find the most popular file's pathname and number of
# occurrences.

import sys

path_dic = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    path, status = data_mapped
    
    if path not in path_dic:
        path_dic[path] = 1
    else:
        path_dic[path] += 1

popular_path = max(path_dic, key=path_dic.get)
print popular_path, "\t", path_dic[popular_path] 

