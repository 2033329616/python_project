#encoding:utf-8

import sys, os, time, baiduocr, screenshot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image


"""用百度搜索的类"""
class Search(object):
	def __init__(self, search_engine_num):
		"""初始化搜索类,search_engine_num搜索引擎号，0代表百度，1代表必应，2代表谷歌"""
		driver_location = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
		self._driver = webdriver.Chrome(driver_location)     # 必须把该exe复制到chrome浏览器安装的位置下
		self._engine_num = search_engine_num
		if self._engine_num == 0:
			self._driver.get('http://www.baidu.com')
		elif self._engine_num == 1:
			self._driver.get('https://cn.bing.com')
		elif self._engine_num == 2:
			self._driver.get('https://www.google.com') 

	def search(self, keywords):
		"""根据文本关键词搜索网页,输入的参数为输入的关键词"""
		
		# start = time.time()			
		# keyword = '有人把金庸小说总结成一句诗,飞雪连天射白鹿,笑书神侠倚碧鸳”鹿指哪一部'
		if self._engine_num == 0:       #使用百度搜索引擎
			self._driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
			self._driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
			self._driver.find_element_by_id('kw').send_keys(keywords)
			self._driver.find_element_by_id('su').send_keys(Keys.ENTER)
			# end = time.time()
			# print('识别字体程序用时：' + str(end - start) + '秒')
		else:
			self._driver.find_element_by_name('q').send_keys(Keys.CONTROL, 'a')
			self._driver.find_element_by_name('q').send_keys(Keys.BACK_SPACE)
			self._driver.find_element_by_name('q').send_keys(keywords)
			self._driver.find_element_by_name('q').send_keys(Keys.ENTER)

def system_init():
	"""初始化"""
	global screen, ocr, search_object, position
	print('请用鼠标截取要处理的区域(q键退出)！')
	screen = screenshot.ScreenShot()      #初始化截图类
	ocr = baiduocr.BaiduOcr()             #初始化文字识别类
	search_object = Search(1)             #初始化搜索类,并选择搜索引擎

	position = screen.get_position()     #获取要截取区域的坐标，只需一次就行！
	print('截图区域为(x,y,w,h)：', position)

def main():
	begin = time.time()   
	screen.window_capture("temp.png", position)       # 开始截图
	if os.path.exists('temp.png'):
		question,answer = ocr.recogniton('temp.png')  # 识别文字
		search_object.search(question)                # 搜索结果
		print(question)
		for index, content  in enumerate(answer):
			print(index + 1, content, end='  ')
	end = time.time()
	print('\n', 'consume time:', end - begin)

if __name__ == '__main__':
	system_init()
	main()

	while True:
		print('='*37)
		text = input('按下回车发起搜索(q键退出):')
		if text == 'q':
			sys.exit()
		main()
