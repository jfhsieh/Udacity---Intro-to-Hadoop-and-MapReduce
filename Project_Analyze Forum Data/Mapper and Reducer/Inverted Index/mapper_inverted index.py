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

reader = csv.reader(sys.stdin, delimiter='\t', quoting= csv.QUOTE_ALL, quotechar = '"')

for line in reader:
	body = line[4].lower()
    if body.find("fantastic") >= 0:
        print "{0}\t{1}".format(line[0], line[4])