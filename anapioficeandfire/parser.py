#!/usr/bin/env python3

import json
from pprint import pprint

import operator

from os import listdir
from os.path import isfile, join


def main ():

	dirs = ('books', 'characters', 'houses')

	for directory in dirs:

		items = []

		files = [f for f in listdir(directory) if isfile(join(directory, f))]
		for filename in files:
			print('loading ' + directory + '/' + filename)
			with open(directory + '/' + filename, 'r') as json_file:
				data = json.load(json_file)
				items += [data]
	
		with open(directory + '.json', 'w') as items_file:
			json.dump(items, items_file)


if __name__ == "__main__":
	main()
