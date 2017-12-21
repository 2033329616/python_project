# encoding:utf-8
# 打开部分网页utf-8乱码？？？？？？？？？？？

import urllib.request as g
import zlib
response=g.urlopen("http://www.qq.com/")
html=response.read()
decompressed_data = zlib.decompress(html ,16+zlib.MAX_WBITS)  

text = decompressed_data.decode('utf8')  
print(text)
# html=html.decode("utf-8")