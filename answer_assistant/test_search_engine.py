#encoding:utf-8


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Search(object):
	def __init__(self):
		"""初始化搜索类"""
		driver_location = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
		self._driver = webdriver.Chrome(driver_location)     # 必须把该exe复制到chrome浏览器安装的位置下
		# self._driver.get('http://www.baidu.com')
		self._driver.get('https://cn.bing.com')
		# self._driver.get('http://www.google.com') #不可用

	def search(self, keywords):
		"""根据文本关键词搜索网页,输入的参数为输入的关键词"""
		
		# start = time.time()			
		# keyword = '有人把金庸小说总结成一句诗,飞雪连天射白鹿,笑书神侠倚碧鸳”鹿指哪一部'


		self._driver.find_element_by_name('q').send_keys(Keys.CONTROL, 'a')
		self._driver.find_element_by_name('q').send_keys(Keys.BACK_SPACE)
		self._driver.find_element_by_name('q').send_keys(keywords)
		self._driver.find_element_by_name('q').send_keys(Keys.ENTER)
		# self._driver.find_element_by_name('q').submit()
		# end = time.time()
		# print('识别字体程序用时：' + str(end - start) + '秒')

if __name__ == '__main__':
	search_o = Search()
	begin = time.time()
	search_o.search('砒霜的别称?')
	end = time.time()
	print(str(end-begin), 's')
	while True:
		print('='*37)
		text = input('按下回车发起搜索(q键退出):')
		if text == 'q':
			sys.exit()
		begin = time.time()
		search_o.search('1+1等于几？')
		end = time.time()
		print(str(end-begin), 's')