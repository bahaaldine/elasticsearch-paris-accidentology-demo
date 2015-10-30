#!/usr/bin/python
import csv
import sys
import json
import urllib2
from datetime import date, datetime

seasons = [('winter', (date(1,  1,  1),  date(1,  3, 20))),
           ('spring', (date(1,  3, 21),  date(1,  6, 20))),
           ('summer', (date(1,  6, 21),  date(1,  9, 22))),
           ('autumn', (date(1,  9, 23),  date(1, 12, 20))),
           ('winter', (date(1, 12, 21),  date(1, 12, 31)))]

def get_season(now):
    if isinstance(now, datetime):
        now = now.date()
    now = now.replace(year=1)
    for season, (start, end) in seasons:
        if start <= now <= end:
            return season
    assert 0, 'never happens'

try:
	filename = sys.argv[1]
	with open(filename, 'rU') as inf, open('../source/accidentology-with-season.csv', 'wb') as outf:
			csvreader = csv.DictReader(inf, delimiter=',')
			fieldnames = csvreader.fieldnames + ['season']
			csvwriter = csv.DictWriter(outf, fieldnames)
			csvwriter.writeheader()

			for node, row in enumerate(csvreader, 1):
				accidentDate = datetime.strptime(row['timestamp'], "%d/%m/%Y %H:%M")
				try:
					csvwriter.writerow(dict(row, season=get_season(accidentDate)))
				except:
					csvwriter.writerow(dict(row, season="winter"))
				
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise




