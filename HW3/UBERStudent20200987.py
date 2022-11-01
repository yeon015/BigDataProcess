#!/usr/bin/python3
import sys
from datetime import datetime, date

inputFile = sys.argv[1]
outputFile = sys.argv[2]

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

with open(inputFile, "rt") as f, open(outputFile, "wt") as fp:
	for line in f:
		arr = line.split(",")
		date = arr[1]
		datetime_date = datetime.strptime(date, '%m/%d/%Y')
		arr[1] = days[datetime_date.weekday()]
		
		fp.write("%s,%s\t%s,%s" % (arr[0], arr[1], arr[2], arr[3]))


