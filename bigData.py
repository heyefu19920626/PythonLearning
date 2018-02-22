
from urllib import request

url = 'http://youku.com'
resource = request.urlopen(url)
html = resource.read()

fn = open('youku.html','w+b')
fn.write(html)
fn.close()
print('downloaded')


if __name__ == '__main__':
	print('main function')
