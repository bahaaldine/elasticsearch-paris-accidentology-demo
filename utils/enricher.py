#!/usr/bin/python
import csv
import sys
import json
import urllib2

try:
	filename = sys.argv[1]
	with open(filename, 'rU') as inf, open('../source/accidentology.csv', 'wb') as outf:
			csvreader = csv.DictReader(inf, delimiter=';', dialect=csv.excel_tab)
			fieldnames = ['timestamp'] + csvreader.fieldnames + ['fullAddress']
			csvwriter = csv.DictWriter(outf, fieldnames)
			csvwriter.writeheader()

			for node, row in enumerate(csvreader, 1):
				timestamp = row["Date"] + " " + row["Hour"]
				fullAddress = row["Address"] + ", " + row["Dept"] + "0" + row["Com"][1:] + " Paris"
				csvwriter.writerow(dict(row, timestamp=timestamp, fullAddress=fullAddress))
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise