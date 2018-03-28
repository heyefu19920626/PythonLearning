import requests
import re


def get_sort_list():
    response = requests.get('http://www.quanshuwang.com/list/2_1.html')
    response.encoding = 'gbk'
    result = response.text
    reg = r'title="(.*?)" href="(.*?)" class="clearfix stitle">'
    novel_list = re.findall(reg, result)
    return novel_list


def get_chapter_list(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    reg = r'png_bg\"><a href="(.*?)"  class="l mr11">'
    nover_urls = re.findall(reg, result)
    response = requests.get(nover_urls[0])
    response.encoding = 'gbk'
    result = response.text
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    chapter_list = re.findall(reg, result)
    return chapter_list


def get_chapter_content(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    reg = r'style5\(\);</script>(.*?)<script'
    chapter_content = re.findall(reg, result, re.S)[0]
    return chapter_content


for nover_name, nover_url in get_sort_list():
    # nover_name = i[0]
    # nover_url = i[1]
    # print(nover_name, nover_url)
    # get_chapter_list(nover_url)
    for chapter_url, chapter_name in get_chapter_list(nover_url):
        print(chapter_name)
        chapter_content = get_chapter_content(chapter_url)
        with open(chapter_name + '.html', 'w') as file:
            file.write(chapter_content)

