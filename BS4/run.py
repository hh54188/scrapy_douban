import urllib2
import sys
sys.path.insert(0, 'libs')
from bs4 import BeautifulSoup

page = urllib2.urlopen("http://www.douban.com/group/beijingzufang/discussion")
soup = BeautifulSoup(page)
collection = soup.select("table.olt td.title a")

for link in collection:
	title = link["title"]
	href = link["href"]

	print title
	print href