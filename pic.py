

import requests
import re
import random
import platform

def spiderPice(html,keyword):
	print('loading...')
	index = 1
	for addr in re.findall('"objURL":"(.*?)"',html,re.S):
		print('crawling... ' + str(addr)[:30] + "...")
		try:
			pics = requests.get(addr,timeout=10)
		except requests.exceptions.ConnectionError:
			print('requests error')
			continue
		if platform.system().lower() == 'windows':
			fq = open('images/' + str(index) + '.jpg','wb')
		else:
			fq = open('/home/IdeaWork/PythonLearning/img/' + str(random.randrange(0,1000,4)) + '.jpg','wb')
		index += 1;
		fq.write(pics.content)
		fq.close()


if __name__ == '__main__':
	print('Main')

	word = input('Please enter the key words you want to crawl.')
	print('word:' + word)
	result = requests.get('https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1519306529980_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=' + word)
	print(result)
	spiderPice(result.text,word)
