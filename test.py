from bs4 import BeautifulSoup
import urllib2
url = "http://www.baidu.com"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html,"html.parse")
for link in soup.find_all('a'):
link.get('href')