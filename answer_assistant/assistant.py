import time, baiduocr, screenshot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

image_directory = "temp.png"
# driver_location = ".\ChromeDriver\chromedriver.exe"
# driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
# 访问百度
driver.get('http://www.baidu.com')

count = 0
screenpath = 'test.png'
while True:
  text = input('按下回车发起搜索')

  start = time.time()
  count = count+1
  
  keyword = '有人把金庸小说总结成一句诗,飞雪连天射白鹿,笑书神侠倚碧鸳”鹿指哪一部'

  driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
  driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
  driver.find_element_by_id('kw').send_keys(keyword)
  driver.find_element_by_id('su').send_keys(Keys.ENTER)

  end = time.time()
  print('程序用时：' + str(end - start) + '秒')