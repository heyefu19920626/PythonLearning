import requests
from bs4 import BeautifulSoup
import re

print('crawling...')

movies = []

for page in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(page * 25) + '&filter='
    print('crawling page ' + str(page + 1))
    print(url)

    html = requests.get(url)
    html.raise_for_status()

    soup = BeautifulSoup(html.text, 'html.parser')
    soup = str(soup)
    # html = open('douban_' + str(page) + '.html','w',encoding='utf-8')
    # html.write(soup)
    # html.close
    # print(soup)
    # title = re.compile('<span class="title">(.*)</span>')
    title = re.compile('<span class="title">(.*)</span>')
    directors = re.compile('导演:(.*)\xa0\xa0\xa0主演')
    movieMessages = re.compile('<span class="title">(.*)</span>(.|\n)*?导演:(.*)<br/>')
    for movieMessage in re.findall(movieMessages, soup):
        for information in movieMessage:
            movieInformation = {}
            movieInformation['movieName'] = movieMessage[0]
            if '主演' in movieMessage[-1]:
                movieInformation['director'] = movieMessage[2].split('主演')[0]
            else:
                movieInformation['director'] = ''.join(movieMessage[-1].split())
        movies.append(movieInformation)
# names = re.findall(title,soup)
# for name in names:
# 	movieInformation = {}
# 	if name.find('/') == -1:
# 		print(name)
# 		movieInformation['movieName'] = name
# 	for director in directors.findall(soup):
# 		movieInformation['director'] = director
# 	movie.append(movieInformation)
# print(name)
# for director in directors.findall(soup):
# 	movieInformation['director'] = director
# print(director)
# for director in re.findall(directors,soup):
# 	print(director)

# movie.append(movieInformation)
index = 1
print(len(movies))
fq = open('movie.txt', 'w', encoding='utf-8')
for movie in movies:
    information = ''
    information = str(index) + '\n电影名称: ' + movie['movieName'] + '\n' + '导演: ' + movie['director'] + '\n'
    fq.write(information)
    index = index + 1
# fq.write(str(movies))
fq.close

# print(movies)
