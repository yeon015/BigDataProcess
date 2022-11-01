#!/usr/bin/python3
import sys
from datetime import datetime, date

inputFile = sys.argv[1]
outputFile = sys.argv[2]

dic = {}

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

with open(inputFile, "rt") as f:
	for line in f:
		region, date, vehicles, trips = line.split(",")
		datetime_date = datetime.strptime(date, '%m/%d/%Y')
		date = days[datetime_date.weekday()]
		trips = trips.strip()
		
		if region not in dic:
			dic[region] = dict()
		if date not in dic[region]:
			dic[region][date] = dict()
			dic[region][date]['vehicles'] = int(vehicles)
			dic[region][date]['trips'] = int(trips)
		else:
			dic[region][date]['vehicles'] += int(vehicles)
			dic[region][date]['trips'] += int(trips)

with open(outputFile, "wt") as fp:
	list = dic.keys()
	for region in list:
		weekList = dic[region].keys()
		for week in weekList:
			fp.write("%s,%s\t%d,%d\n" % (region, week, dic[region][week]['vehicles'], dic[region][week]['trips'])) 

