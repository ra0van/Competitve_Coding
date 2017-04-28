#https://www.hackerrank.com/contests/capture-the-flag/challenges/infinite-links
from bs4 import BeautifulSoup
import requests
import json
import re

def hack():
	global base
	global ext
	global visited
	global unvisited
	global secret

	while len(unvisited)>0:
		url = unvisited[0]
		visited.append(url)
		print 'reaching '+url + ext
		response = requests.get(base + url + ext)
		# print response.text
		soup = BeautifulSoup(response.text,'html.parser')
		for key in soup.findAll('font'):
			m = re.search('</b>(.+?)</font',str(key))
			if m:
				secret_key = m.group(1)
				secret.append(secret_key)
				print 'found a key :' + secret_key
		for key in  soup.findAll('a'):
			m = re.search('>(.+?)</a>',str(key))
			if m:
				new_url = m.group(1)
				# print new_url
				if new_url not in visited and new_url not in unvisited and new_url != url:
					unvisited.append(new_url)
					print 'found new url :' + new_url
		unvisited.remove(url)


base = 'https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/'
visited = []
unvisited = ['qds']
secret = []
ext = '.html'
# secret_regex = '</b>*</font>'

while len(unvisited)>0:
	try:
		hack()
	except :
		print 'error : '+unvisited[0]



print visited
# print secret

f= open('infinte.txt','w')
for key in sorted(secret):
	f.write(key+'\n')
f.close()
