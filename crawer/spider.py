import requests
import re


def get_sort_list(url):
    response = requests.get(url)
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


def get_total_page(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    reg = r'class="last">(.*?)</a><kbd>'
    total_page = re.findall(reg, result)[0]
    return int(total_page)


for i in range(1, 12):
    url = "http://www.quanshuwang.com/list/" + str(i) + "_1.html"
    total_page = get_total_page(url)
    for j in range(1, total_page + 1):
        page_url = "http://www.quanshuwang.com/list/" + str(i) + "_" + str(j) + ".html"
        for nover_name, nover_url in get_sort_list(page_url):
            # nover_name = i[0]
            # nover_url = i[1]
            # print(nover_name, nover_url)
            # get_chapter_list(nover_url)
            for chapter_url, chapter_name in get_chapter_list(nover_url):
                print(chapter_name)
                try:
                    chapter_content = get_chapter_content(chapter_url)
                except:
                    print("错误网址:" + chapter_url)
                with open(nover_name + '.html', 'a') as file:
                    file.write(chapter_name)
                    file.write(chapter_content)
