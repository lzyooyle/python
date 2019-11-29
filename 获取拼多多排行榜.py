import requests
import time
import re
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

if __name__ == '__main__':
	list_url = []
	i = 2080
	while i < 9999:
		i = i + 1;
		url='https://mobile.yangkeduo.com/sjs_cat_rank_list.html?list_id='+str(i)+'010401&__list_version=2&activeTab=0'
		#设置请求头信息
		headers = {
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
		}
		req = requests.get(url=url,headers=headers)
		req.encoding='utf-8'
		html=req.text
		bf = BeautifulSoup(html,'html.parser')
		targets_url_1 = bf.find_all("div", class_="sc-dnqmqq cgCvSV")
		targets_url_1=re.sub('[\t\n]',"",re.sub(r'<[^>]+>',"",str(targets_url_1))).strip('[').strip(']')
		print(targets_url_1)
		#保存名字链接
		with open('data5.txt','a') as f: 
			if targets_url_1!='':		
				f.write(targets_url_1+url)
				f.write('\n')
	print('下载完成！')### unterminated keywords ###### unterminated keywords### unterminated keywords ###### unterminated keywords ###### unterminated keywords ###