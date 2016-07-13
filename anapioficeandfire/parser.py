#!/usr/bin/env python3

import json
from pprint import pprint

import operator

from os import listdir
from os.path import isfile, join


def combine_all():

	removed = (6,4,9,7,8,11,1,5,3,10)

	dirs = ('books', 'characters', 'houses')
	for directory in dirs:
		items = []
		files = [f for f in listdir(directory) if isfile(join(directory, f))]
		for filename in files:
			with open(directory + '/' + filename, 'r') as json_file:
				data = json.load(json_file)
				if 'name' in data and data['name']:

					removedkeys = []
					for r in removed:
						url = 'http://anapioficeandfire.com/api/characters/' + str(r)
						for k in data:
							if isinstance(data[k], str):
								if len(data[k]) > len('http://anapioficeandfire.com/api/characters/'):
									print(data[k])
								if data[k] == url:
									removedkeys += [k]
							elif isinstance(data[k], list):
								pass
								#for item in data[k]:
								#	print('\t' + item)
					if len(removedkeys) > 0:
						print('removedkeys:', removedkeys)

					#for r in removed:
					#	for k in data:
					#		if type(data[k]) == type(dict):
					#			for j in data[k]:
					#				if 'http://anapioficeandfire.com/api/characters/' in data[k][j]:
					#					print('removing ' + str(r))
					#		elif type(data[k]) == type(list):
					#			for line in data[k]:
					#				if 'http://anapioficeandfire.com/api/characters/' in line:
					#					print('removing ' + str(r))
					#		elif type(data[k]) == type(str):
					#			if 'http://anapioficeandfire.com/api/characters/' in data[k]:
					#				print('removing ' + str(r))

					items += [data]
				else:
					print(directory + '/' + filename)

		with open(directory + '.json', 'w') as items_file:
			json.dump(items, items_file)


def main():
	combine_all()
	#with open('characters.json') as datafile:
	#	data = json.load(datafile)
	#	d = {}
	#	for character in data:
	#		id = int(character['url'].split('/').pop())
	#		if character['name']:
	#			d[id] = character['name']
	#	for k in d:
	#		print(str(k) + ":" + d[k])


if __name__ == "__main__":
	main()
