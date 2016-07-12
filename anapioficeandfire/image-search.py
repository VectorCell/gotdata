#!/usr/bin/env python3


import urllib.request
import re


PREFIX = 'http://awoiaf.westeros.org'


def main():

	print("#!/bin/bash\n")

	urls = [line.rstrip('\n') for line in open('urls.txt', 'r')]
	characters = {}
	for line in open('characters.txt', 'r'):
		spl = line.rstrip('\n').split(':')
		characters[int(spl[0])] = {'name': spl[1]}

	for k in characters:
		for url in urls:
			if characters[k]['name'].replace(' ', '_') in url:
				if 'url' not in characters[k]:
					characters[k]['url'] = url
				else:
					if characters[k]['name'] == 'Will':
						continue
					if characters[k]['name'] == 'Viserys I':
						continue
					if characters[k]['name'] == 'Cass':
						continue
					if characters[k]['name'] == 'Drogo':
						continue
					if characters[k]['name'] == 'Hal':
						continue
					if characters[k]['name'] == 'Clegane':
						continue
					if characters[k]['name'] == 'Bael':
						continue
					if characters[k]['name'] == 'Lann':
						continue
					if characters[k]['name'] == 'Walder':
						continue
					if characters[k]['name'] == 'Walder Frey':
						continue
					#print('for character', characters[k]['name'], 'avoiding overwriting', characters[k]['url'], 'with', url)

	remove = [k for k in characters if 'url' not in characters[k]]
	for k in remove:
		del characters[k]

	maximum = 15000
	for k in characters:
		#print('character:', k, '::', characters[k])
		unique = 0

		req = urllib.request.Request(characters[k]['url'], headers={'User-Agent': 'Mozilla/5.0'})
		page = urllib.request.urlopen(req).read().decode('utf-8')

		lines = []
		for line in page.split('\n'):
			if 'File:' in line and 'href' in line and 'thumb' not in line:
				line = line.split('"')[1]
				lines += [line]

		images = []
		for line in lines:
			req2 = urllib.request.Request(PREFIX + line, headers={'User-Agent': 'Mozilla/5.0'})
			page2 = urllib.request.urlopen(req2).read().decode('utf-8')
			lines2 = []
			for line2 in page2.split('\n'):
				if 'fullMedia' in line2:
					lines2 += [line2.split('"')[3]]
			for line2 in lines2:
				images += [PREFIX + line2]

		for image in images:
			if unique == 0:
				print('wget', '-O', str(k) + ".jpg", image)
			else:
				print('wget', '-O', str(k) + "_" + str(unique) + ".jpg", image)
			unique += 1

		maximum -= 1
		if maximum == 0:
			break


if __name__ == '__main__':
	main()
