#!/usr/bin/python

import sys
import json
import urllib2
import time
import os
import ssl


# Init from website.
servicePublicId="da8488da9b5df26d32ca58c6d6a7973bedd5d98ad052d62b468d3b04b080ea25"

# Read locations from json files.
def read_location_json(filename):
	with open(filename) as f:
  		location_objs = json.load(f)
  		return location_objs

# Fetch availibe times from https://onlinebusiness.icbc.com/qmaticwebbooking/#/
# Only support knowledge test
def fetch_available_times(loc):
	# Fix SSL error
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE
	url = "https://onlinebusiness.icbc.com/qmaticwebbooking/rest/schedule/branches/{0}/dates;servicePublicId={1};customSlotLength=15"
	url =  url.format(loc['id'], servicePublicId)
	response = urllib2.urlopen(url, context=ctx)
	content = response.read()
	return json.loads(content)

# Match month.
def is_match(times, month):
	for time in times:
		d = time['date']
		if d.startswith(month):
			return True
	return False

def send_notification(times, loc):
	# TODO: add notification to mobile or desktop.
	make_bell_sound()
	print 'Found match date at [', loc["name"],']'
	print 'Available times'
	for t in times:
		print t['date']

# make a sound in your computer 
def make_bell_sound():
	os.system("say 'ICBC appointment found.'")
	os.system("say 'ICBC appointment found.'")
	os.system("say 'ICBC appointment found.'")

def main():
	expectMonth = sys.argv[2]
	print 'start detecting appointments in', expectMonth, '...'
	loc_file = sys.argv[1]
	locations = read_location_json(loc_file)
	try_time = 1
	for loc in locations:
		while True:
			times = fetch_available_times(loc)
			if is_match(times, expectMonth):
				send_notification(times, loc)
				break
			time.sleep(3)
			try_time += 1 
			sys.stdout.write(".")
			sys.stdout.flush()


if __name__ == "__main__":
    # execute only if run as a script
    main()
