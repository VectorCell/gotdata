#!/usr/bin/env python3

import json
from pprint import pprint

import operator

from os import listdir
from os.path import isfile, join

import urllib.request


def read_other_api():
	response = urllib.request.urlopen('http://itstimetoduel.me/apiv1/cards')
	data = json.loads(response.read().decode('utf-8'))
	print(type(data))
	for item in data:
		d = {}
		d['id'] = item[0]
		d['card_type'] = item[-7]
		d['name'] = item[4]
		d['text'] = item[5]
		d['family'] = item[4567]
		print(item)
		for k in d:
			print(k + " :: " + d[k])
		print(d)
		print()


def combine_all():

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


def main():
	with open('characters.json') as datafile:
		data = json.load(datafile)
		d = {}
		for character in data:
			id = int(character['url'].split('/').pop())
			if character['name']:
				d[id] = character['name']
		for k in d:
			print(str(k) + ":" + d[k])


if __name__ == "__main__":
	read_other_api()
