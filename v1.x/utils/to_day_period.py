#!/usr/bin/python
import csv
import sys
import json
import urllib2
from datetime import date, datetime

seasons = [('morning', (datetime.strptime("1900-01-01 06:00", "%Y-%m-%d %H:%M"), datetime.strptime("1900-01-01 11:29", "%Y-%m-%d %H:%M"))),
           ('lunch', (datetime.strptime("1900-01-01 11:29", "%Y-%m-%d %H:%M"), datetime.strptime("1900-01-01 14:00", "%Y-%m-%d %H:%M"))),
           ('afternoon', (datetime.strptime("1900-01-01 14:01", "%Y-%m-%d %H:%M"), datetime.strptime("1900-01-01 18:00", "%Y-%m-%d %H:%M"))),
           ('evening', (datetime.strptime("1900-01-01 18:01", "%Y-%m-%d %H:%M"), datetime.strptime("1900-01-01 23:00", "%Y-%m-%d %H:%M"))),
           ('overNight', (datetime.strptime("1900-01-01 23:01", "%Y-%m-%d %H:%M"), datetime.strptime("1900-01-01 05:00", "%Y-%m-%d %H:%M")))]

def get_period_of_the_day(now):
  for period, (start, end) in seasons:
		if start <= now <= end:
			print period
			return period

try:
	filename = sys.argv[1]
	with open(filename, 'rU') as inf, open('../source/accidentology-with-day-period.csv', 'wb') as outf:
			csvreader = csv.DictReader(inf, delimiter=',')
			fieldnames = csvreader.fieldnames + ['periodOfDay']
			csvwriter = csv.DictWriter(outf, fieldnames)
			csvwriter.writeheader()

			for node, row in enumerate(csvreader, 1):
				accidentDate = datetime.strptime(row['timestamp'], "%d/%m/%Y %H:%M")
				accidentTime = datetime.strptime("1900-01-01 "+str(accidentDate.hour)+":"+str(accidentDate.minute), "%Y-%m-%d %H:%M")
				csvwriter.writerow(dict(row, periodOfDay=get_period_of_the_day(accidentTime)))

except:
    print "Unexpected error:", sys.exc_info()[0]
    raise