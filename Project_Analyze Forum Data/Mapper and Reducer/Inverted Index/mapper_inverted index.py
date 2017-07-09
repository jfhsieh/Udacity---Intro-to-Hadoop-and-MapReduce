#!/usr/bin/python

# Format of each line is:
# "id"	"title"	"tagnames"	"author_id"	"body"	"node_type"	"parent_id"	
# "abs_parent_id"	"added_at"	"score"	"state_string"	"last_edited_id"	
# "last_activity_by_id"	"last_activity_at"	"active_revision_id"	"extra"	
# "extra_ref_id"	"extra_count"	"marked"
#
# The mapper will have element body contain the string "fantastic" and
# element id.
# The standard output is separated by a tab.

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    regex = r'\b(fantastic)\b'
    if re.search(regex, line[4], re.IGNORECASE):
    	print "{0}\t{1}".format(line[0], "fantastic")

    regex = r'\b(fantastically)\b'
    if re.search(regex, line[4], re.IGNORECASE):
    	print "{0}\t{1}".format(line[0], "fantastically")