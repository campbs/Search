#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
from operator import itemgetter
import porter2


def createWordsDict(fileName):
	inputFile = open(fileName).read()
	wordsDict = {}
	delims= r'[ "\t,;.?!\r\n]+'
	temp = re.split(delims,inputFile)
	for token in temp:
		token = token.lower()
		if token not in wordsDict:
			wordsDict[token] = 1
		else:
			wordsDict[token] += 1
	return wordsDict

def main():
	try:
		k = int(sys.argv[2])
		fileName = sys.argv[1]
		wordsDict = createWordsDict(fileName)
		wordsDict = sorted(wordsDict.items(), key=itemgetter(1), reverse=True)[:k]


		# print '\nHi'
		for tuple in wordsDict:
			for token in tuple:
				print porter2.stem(token)
				break;
	except:
		print "Error"

if __name__ == '__main__':
	main()

#Author: Piyush Arora
#Have fun, keep coding
