#encoding:utf-8

from HandleJs import Py4Js   # 计算tk值的库
import urllib.request
import urllib.parse
import json

class translate(object):
	"""翻译类定义"""
	def __init__(self):
		self._content = ''

	def google_translate(self, content):
		"""
		功能：谷歌翻译
		参数：传入要翻译的内容
		"""
		self._content = content.replace('\n', ' ')     # 待翻译的文本,除去回车提升翻译质量
		self._result = ''           # 翻译的结果

		# 判断要翻译的内容是否超出上限
		if len(self._content) > 4891:
			return '超出文本上限，请缩减待翻译文本！'
		# print(self._content)
		# self._content = urllib.parse.quote(self._content)  # 将文本url编码

		# 判断英汉互译的方向
		isCharacter = lambda x: ((x >= 'a') and (x <= 'z')) or ((x >= 'A') and (x <= 'Z'))  #是字母返回True
		if isCharacter(self._content[0]):
			sl = 'en'        # 从英语
			tl = 'zh-CN'     # 到汉语
		else:
			sl = 'zh-CN'
			tl = 'en'
		# 计算文本的tk值
		js = Py4Js()                  # 初始化计算类
		tk = js.getTk(self._content)  # 获得tk值

		# 生成get请求的url
		url = "http://translate.google.cn/translate_a/single?client=t"\
		"&sl=%s&tl=%s&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca"\
		"&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1"\
		"&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s" % (sl, tl, tk)
		# print(url)
		# 进行post请求
		headers = {}
		headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
		data = {}
		data['q'] = self._content
		data = urllib.parse.urlencode(data).encode("utf-8")
		# print(data)
		req = urllib.request.Request(url=url, data=data, headers=headers)   # post请求
		# print(req)
		reponse = urllib.request.urlopen(req)
		html = reponse.read().decode('utf-8')
		target = json.loads(html)
		for index in range(len(target[0])):
			# print('-----------------------------------')
			# print(index)
			print(target[0][index][0],end=' ')  #输出结果中查看其结构，然后选定索引方式


if __name__ == '__main__':
	tran = translate()     # 实例化一个类
	content = """hello world.you are familhelworld.you are family"""
	# print(content)
	tran.google_translate(content)

	# print(ord('a'), ord('z'),'|', ord('A'), ord('Z'))   # 97 122 | 65 90
	# # for i in range(65, 90):
	# # 	print(i)

	# # 下面的两种方式均能判断是否是字母
	# isCharacter = lambda x: ((x >= 'a') and (x <= 'z')) or ((x >= 'A') and (x <= 'Z'))
	# # if ord(self._content[0]) in range(97, 123) or ord(self._content[0]) in range(65, 91)：
	# # 	print('this is a character.')

	# print(isCharacter(''))
