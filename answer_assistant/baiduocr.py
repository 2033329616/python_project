#encoding:utf-8

from aip import AipOcr

"""百度文字识别的类"""
class BaiduOcr(object):
	def __init__(self):
		"""初始化类"""
		
		""" 你的 APPID AK SK """
		self._APP_ID = '10684836'
		self._API_KEY = 'ebjRMkjywXohjxk6IHKWBMxi'
		self._SECRET_KEY = 'YEiDYMN4FgtDWRHNAWhxQClNn99Ciw6X'		
		self._client = AipOcr(self._APP_ID, self._API_KEY, self._SECRET_KEY)

	def recogniton(self, filePath):
		"""识别图像中的文字，传入参数为图像路径；返回识别到的问题与答案
		这里主要用到百万英雄中，所以返回参数为问题和答案
		"""
		with open(filePath, 'rb') as img_file:
			""" 调用通用文字识别, 图片参数为本地图片 """
			content = self._client.basicGeneral(img_file.read())

			question = ''            #问题字符串
			optional_answer = []     #备选答案列表

			for index in content['words_result'][:-3]:  #后面三个是备选答案，所以问题是前面的字符串
				question = question + index['words']
			# print(question[1:])

			for index in content['words_result'][-3:]:
				optional_answer.append(index['words'])
			# print(optional_answer)
			# print(question)
			# print(optional_answer)
			try:                    #防止'.'没有识别出来
				last_question = question.split('.', 1)[1]
				return last_question, optional_answer
			except IndexError as err:
				# print(str(err))
				return question[1:], optional_answer

if __name__ == '__main__':
	ocr = BaiduOcr()  #初始化文字识别类
	q,a = ocr.recogniton('test.png')
	print(q)
	print(a)