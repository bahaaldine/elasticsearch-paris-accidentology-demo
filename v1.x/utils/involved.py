#!/usr/bin/python
import csv
import sys
import json
import urllib2
from datetime import date, datetime

try:
	filename = sys.argv[1]
	with open(filename, 'rU') as inf, open('../source/accidentology-with-involved.csv', 'wb') as outf:
			csvreader = csv.DictReader(inf, delimiter=',')
			fieldnames = csvreader.fieldnames + ['involvedCount']
			csvwriter = csv.DictWriter(outf, fieldnames)
			csvwriter.writeheader()

			for node, row in enumerate(csvreader, 1):
				if row['F']:
					csvwriter.writerow(dict(row, involvedCount=3))
				elif row['D']:
					csvwriter.writerow(dict(row, involvedCount=2))
				elif row['responsability']:
					csvwriter.writerow(dict(row, involvedCount=1))
				
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise