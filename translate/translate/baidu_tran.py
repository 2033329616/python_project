import urllib.request
import urllib.parse
import json


content = """我是中国人，我是中国人我是中国人我是中国人我是中国人v我是中国人我是中国人v
我是中国人我是中国人我是中国人我是中国人我是中国人我是中国人我是中国人"""



data = {}
if ord(content[0]) in range(97,123) or ord(content[0]) in range(65,91): #是否是字母/英文
    data['from'] = 'en'
    data['to'] = 'zh'
else:                  #中文
    data['from'] = 'zh'
    data['to'] = 'en'
data['query'] = content.replace('\n', ' ')
data['transtype'] = 'translang'
data['simple_means_flag'] = '3'
data = urllib.parse.urlencode(data).encode('utf-8')

head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3067.6 Safari/537.36'

url = 'http://fanyi.baidu.com/v2transapi'
req = urllib.request.Request(url,data,head)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')

target = json.loads(html)

# print('翻译结果是：%s'%(target['trans_result']['data'][0]['dst']))
# print(target['trans_result'])
# print('------------------------------------------------')
# # 'from', 'to', 'domain', 'type', 'status', 'data', 'phonetic', 'keywords'
# print(target['trans_result'].keys())
# print('--------------------------------------------------')
# print(target['trans_result'].values())
# for key in target['trans_result']:
#     print('------------------------------------------------')
#     print('key=:', key)
#     print(target['trans_result'][key])
# print(target['trans_result']['data'])
# print(len(target['trans_result']['data']))
print(content.replace('\n', ' '))
for i in range(len(target['trans_result']['data'])):
    print(target['trans_result']['data'][i]['dst'], end='')