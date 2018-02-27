# crawls description and category for a youtube video

import urllib2
from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import time
import os
from bs4 import BeautifulSoup
from multiprocessing import Process
import pickle

#os.environ['http_proxy'] = "http://172.16.2.30:8080/"
#os.environ['https_proxy'] = "https://172.16.2.30:8080/"


def crawl_youtube(id_):
	url = 'https://www.youtube.com/watch?v='+str(id_)
	information = {}
	information['view_count'] = ''
	information['desc'] = ''
	information['category'] = ''
	information['like_count'] = ''
	information['dislike_count'] = ''
	information['publish_date'] = ''

	#try:
	txt = ''
	temp = []
	request = urllib2.Request(url)
	txt = urllib2.urlopen(request).read()
	
	soup = BeautifulSoup(txt)

	for p in soup.findAll("div",{"class":"watch-view-count"}):
		information['view_count'] = p.text.strip().split(" ")[0]

	for p in soup.findAll("div",{"id":"watch-description-text"}):
		information['desc'] = p.text.strip()


	for p in soup.findAll("ul",{"class":"content watch-info-tag-list"}):
		information['category'] = p.text.strip()

	#for p in soup.findAll("span",{"class":"like-button-renderer actionable "}):
	for q in soup.findAll("span",{"class":"like-button-renderer"}):
		#print q.text.strip()
		for p in q.findAll("span",{"class":"yt-uix-button-content"}):
			temp.append(p.text.strip())
	information['like_count'] = temp[0]
	information['dislike_count'] = temp[3]

	for p in soup.findAll("strong",{"class":"watch-time-text"}):
		information['publish_date'] = p.text.strip()

	

	return information




	
if __name__=="__main__":

		
	print crawl_youtube('0Q3D-hxX-Gs')

