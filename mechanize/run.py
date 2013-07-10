import re
import mechanize

br = mechanize.Browser()
br.open("http://www.douban.com/")
print br.title()