
import requests
from bs4 import BeautifulSoup
import re



print('crawling...')

for page in range(10):
	url = 'https://movie.douban.com/top250?start=' + str(page*25) + '&filter='
	print('crawling page ' + str(page + 1))
	print(url)

	html = requests.get(url)
	html.raise_for_status()

	soup = BeautifulSoup(html.text,'html.parser')
	soup = str(soup)
	title = re.compile('<span class="title">(.*)</span>')
	directors = re.compile('(导演:.*)主演')
	for director in re.findall(directors,soup):
		print(director)
	# names = re.findall(title,soup)
	# for name in names:
	# 	if name.find('/') == -1:
	# 		print(name)