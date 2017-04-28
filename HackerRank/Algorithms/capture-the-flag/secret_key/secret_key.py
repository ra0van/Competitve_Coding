#https://www.hackerrank.com/contests/capture-the-flag/challenges/secret-key
from bs4 import BeautifulSoup
import requests
import json
import mechanize

key_url = 'https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/secret/key.json'
secret_url = 'https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/secret/'

news_id = 'news-body white'

r = requests.get(key_url)
# print r.text
base = "secret_json/"
ext = ".json"
news = []
i = 1
for key,value in json.loads(r.text).iteritems():
	url = secret_url + base + key + ext
	response = requests.get(url)
	# for key,value in json.loads(response.text).iteritems():
	# 	print key,value
	news.append(json.loads(response.text)['news_title'])
	print i,json.loads(response.text)['news_title']
	i+=1
# print sorted(news)

f= open('secrext.txt','w')
for key in sorted(news):
	f.write(key+'\n')
f.close()

