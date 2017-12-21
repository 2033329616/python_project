# encoding:utf-8

# from HandleJs import Py4Js   # 计算tk值的库
# import sys
# sys.path.append('.\\translate')    #为了导入HandleJs模块

# from HandleJs import Py4Js
import urllib.request
import urllib.parse
import HandleJs
import json

"""英汉汉英互译的类"""
class translate(object):
	def __init__(self):
		# 初始化翻译类
		self._content = ''
		self._data = {}  # 配置翻译的参数

	def baidu_translate(self, content):
		"""
			功能：百度翻译
			参数：content待翻译的内容
        """
		self._content = content.replace('\n', ' ')  # 要翻译的内容,# 将文档字符串中的回车删除，提高翻译质量
		self._result = ''        # 翻译的结果
		self._data = {}          # 需再次赋值为空，否则再次调用时程序会卡死！！！！！
		url = "http://fanyi.baidu.com/v2transapi"
		if ord(self._content[0]) in range(97, 123) or ord(self._content[0]) in range(65, 91):  # 是否是字母/英文
			self._data['from'] = 'en'
			self._data['to'] = 'zh'
		else:  # 中文
			self._data['from'] = 'zh'
			self._data['to'] = 'en'
		self._data['query'] = self._content     #要查询的内容
		self._data['transtype'] = 'translang'
		self._data['simple_means_flag'] = '3'
		self._data = urllib.parse.urlencode(self._data).encode("utf-8")
		# print(self._data)
		head = {}
		head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3067.6 Safari/537.36'
		req = urllib.request.Request(url, self._data, headers=head)
		response = urllib.request.urlopen(req)
		html = response.read().decode('utf-8')
		target = json.loads(html)
		for i in range(len(target['trans_result']['data'])):
			# print(target['trans_result']['data'][i]['dst'], end='')
			self._result = self._result + ' ' +target['trans_result']['data'][i]['dst']   # 翻译结果拼接
			# print(self._result)
		return self._result

		# response = urllib.request.urlopen(url, self._data)
		# html = response.read().decode("utf-8")
		# target = json.loads(html)
		# tgt = target['trans_result']['data'][0]['dst']
		# print("翻译的结果是：%s"% tgt)
		# print(type(tgt))
		# return tgt

	def google_translate(self, content):
		"""
		功能：谷歌翻译
		参数：传入要翻译的内容
		"""
		self._content = content.replace('\n', ' ')     # 待翻译的文本,除去回车提升翻译质量
		self._result = ''           # 翻译的结果

		# 判断要翻译的内容是否超出上限
		# if len(self._content) > 4891:
		# 	return '超出文本上限，请缩减待翻译文本！'
		# print(self._content)

		# 判断英汉互译的方向
		isCharacter = lambda x: ((x >= 'a') and (x <= 'z')) or ((x >= 'A') and (x <= 'Z'))  #是字母返回True
		if isCharacter(self._content[0]):
			sl = 'en'        # 从英语
			tl = 'zh-CN'     # 到汉语
		else:
			sl = 'zh-CN'
			tl = 'en'
		# 计算文本的tk值
		js = HandleJs.Py4Js()                  # 初始化计算类
		tk = js.getTk(self._content)  # 获得tk值

		# 生成post请求的url
		url = "http://translate.google.cn/translate_a/single?client=t"\
		"&sl=%s&tl=%s&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca"\
		"&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1"\
		"&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s" % (sl, tl, tk)
		# print(url)
		# 进行post请求
		headers = {}
		headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
		self._data = {}
		self._data['q'] = self._content
		self._data = urllib.parse.urlencode(self._data).encode("utf-8")  #将待翻译的内容编码为

		req = urllib.request.Request(url=url, data=self._data, headers=headers)   # post请求
		# print(req)
		reponse = urllib.request.urlopen(req)
		html = reponse.read().decode('utf-8')
		target = json.loads(html)
		# print(target)
		for index in range(len(target[0])-1):   #
			# print('-----------------------------------')
			# print(index)
			# print(target[0][index][0])
			# print(target[0][index][0],end='')  #输出结果中查看其结构，然后选定索引方式
			self._result = self._result + ' ' + target[0][index][0]
		return self._result

if __name__ == '__main__':
	trans = translate()   # 定义翻译类
	result = trans.google_translate("""Equations (3) and (7) are called the optimality equations
	of dynamic programming whichn""")
	print(result)
