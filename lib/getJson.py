#!/usr/bin/env python

import urllib, simplejson
import cPickle, os

MTGDBURLCARDS = 'http://api.mtgdb.info/cards/'
MTGDBURLSETS = 'http://api.mtgdb.info/sets/'
MTGDBURLRARITIES = 'http://api.mtgdb.info/rarity/'
MTGDBURLTYPES = 'http://api.mtgdb.info/types/'
MTGDBURLSUBTYPES = 'http://api.mtgdb.info/subtypes/'
def getData(url):
	url = urllib.urlopen(url)
	data = url.read()
	url.close()
	return data
	
def decodeData(data):
	return simplejson.loads(data)
	
def dumpData(data, path):
	with open(path, 'wb') as f:
		cPickle.dump(data, f)

def loadData(path):
	with open(path, 'rb') as f:
		return cPickle.load(f)
		

def run(url, path):
	data = decodeData(getData(url))
	dumpData(data, path)
	return data
	
def save(data, path):
	dumpData(data, path)
	
def load(path):
	return loadData(path)
	


def main():
	path = os.getcwd()
	run(MTGDBURLCARDS, path)

if __name__ == '__main__':
	main()

	