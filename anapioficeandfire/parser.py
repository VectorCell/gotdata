#!/usr/bin/env python3

import json
from pprint import pprint

import operator

from os import listdir
from os.path import isfile, join


#CHARACTER_JON_SNOW = 'characters/583.json'


def main ():

	dirs = ('books', 'characters', 'houses')

	locations = set()

	for directory in dirs:
		files = [f for f in listdir(directory) if isfile(join(directory, f))]
		for filename in files:
			with open(directory + '/' + filename) as json_file:
				data = json.load(json_file)
			if 'seats' in data and len(data['seats']) > 0:
				for seat in data['seats']:
					locations |= {seat};

	for location in locations:
		print(location)


if __name__ == "__main__":
	main()
