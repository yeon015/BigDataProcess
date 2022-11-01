#!/usr/bin/python3
import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

dic = {}

with open(inputFile, "rt") as f:
	for line in f:
		arr = line.split("::")
		genre = arr[2]
		
		if genre.find('|') != -1:
			genre_list = genre.split("|")
			for i in genre_list:
				i = i.strip()
				if i not in dic:
					dic[i] = 1
				else:
					dic[i] += 1
		else:
			genre = genre.strip()
			if genre not in dic:
				dic[genre] = 1
			else:
				dic[genre] += 1
print(dic)
with open(outputFile, "wt") as fp:
	keyList = dic.keys()
	for i in keyList:
		fp.write("%s %s\n" % (i, dic[i]))
