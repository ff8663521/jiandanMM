import random

UAList = ['Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
,'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
,'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'
,'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
,'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
,'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
,'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'
,'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'
,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
,'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)'
,'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'
,'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
,'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)'
,'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'
,'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'
,'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)'
,'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)']
 
UANameList=['afari 5.1 – MAC',
'safari 5.1 – Windows',
'IE 8.0',
'IE 7.0',
'IE 6.0',
'Firefox 4.0.1 – MAC',
'Firefox 4.0.1 – Windows',
'Opera 11.11 – MAC',
'Opera 11.11 – Windows',
'Chrome 17.0 – MAC',
'腾讯TT',
'世界之窗（The World） 2.x',
'世界之窗（The World） 3.x',
'搜狗浏览器 1.x',
'360浏览器',
'Avant',
'Green Browser']

def getRandomUA():
     return random.choice(UAList)
