#!/usr/bin/python

# Format of each line is:
# %h %l %u %t \"%r\" %>s %bt
# %h is the IP address of the client
# %l is identity of the client, or "-" if it's unavailable
# %u is username of the client, or "-" if it's unavailable
# %t is the time that the server finished processing the request. The format is [day/month/year:hour:minute:second zone]
# %r is the request line from the client is given (in double quotes). It contains the method, path, query-string, and protocol or the request.
# %>s is the status code that the server sends back to the client. You will see see mostly status codes 200 (OK - The request has succeeded), 304 (Not Modified) and 404 (Not Found).
# %b is the size of the object returned to the client, in bytes. It will be "-" in case of status code 304.

import sys
import re

for line in sys.stdin:
	line = line.strip()
	regex = '([(\d\.)]+) (.*?) (.*?) \[(.*?)\] \"(.*?)\" (.*?) (.*)'

	data = list(re.match(regex, line).groups())

		ip, identity, username, time, request, status, size = data
		print "{0}\t{1}".format(ip, status)
