#!/usr/bin/python
import csv
import sys
import json
import urllib2
import urllib
import time

apiKey = ['GOOGLE_API_KEY']
apiKeyIndex = 0

def getGeolocalisationData(url, attempts=0, success=False):
	global apiKeyIndex
	while success != True and attempts < 3:
		raw_result = json.load(urllib2.urlopen(url))
		attempts += 1
		status = raw_result["status"]
		if status == "OVER_QUERY_LIMIT":
			time.sleep(2)
			getGeolocalisationData(url, attempts, success)
			continue
		success = True
	if attempts == 3:
		print "Daily limit has been reached"
		apiKeyIndex = apiKeyIndex+1
		if apiKeyIndex >= len(apiKey):
			print "No API KEY anymore"
			raise
		else:
			print "Switch API key to --> ", apiKey[apiKeyIndex]
			url = "https://maps.googleapis.com/maps/api/geocode/json?key="+apiKey[apiKeyIndex]+"&sensor=false&address="+urllib.urlencode(query_string).replace("fullAddress=", "")
			getGeolocalisationData(url, attempts, success)
	else: 
		return raw_result


try:
	with open('../source/accidentology-with-geo-1.csv', 'rU') as inf, open('../source/accidentology-with-geo-3.csv', 'wb') as outf:
		csvreader = csv.DictReader(inf, delimiter=',')
		#fieldnames = csvreader.fieldnames + ['latitude'] + ['longitude']
		csvwriter = csv.DictWriter(outf, csvreader.fieldnames)
		#csvwriter.writeheader()

		cache = {}
		for node, row in enumerate(csvreader, 1):
			query_string = {}
			query_string['fullAddress'] = row['fullAddress']
			raw_result = {}
			if row['fullAddress'] in cache:
				csvwriter.writerow(dict(row, latitude=cache[row['fullAddress']]['lat'], longitude=cache[row['fullAddress']]['lng']))
			else:
				url = "https://maps.googleapis.com/maps/api/geocode/json?key="+apiKey[apiKeyIndex]+"&sensor=false&address="+urllib.urlencode(query_string).replace("fullAddress=", "")
				raw_result = getGeolocalisationData(url)
				if not raw_result:
					print "aborting process"
					raise
				else:
					location = raw_result['results'][0]['geometry']['location']
					cache[row['fullAddress']] = location
					csvwriter.writerow(dict(row, latitude=location['lat'], longitude=location['lng']))
except:
  print "Unexpected error:", sys.exc_info()[0]
  raise