import urllib.request
import os
import time
import re
import user_agent_list as ua
import traceback
import mylogger

logger = mylogger.MyLogger(1,'themain').getlog()

def setDir(path,foldName):
	#创建工作目录
    try:
        os.mkdir(path+'/'+foldName)
    except FileExistsError:
        logger.debug(foldName+'目录已存在')
    else :
        logger.debug(foldName+'目录创建完成')
		
    #变更工作目录为新创建文件夹
    os.chdir(path+'/'+foldName)     

def openTheUrl(url):
    '''
          url为将要打开的地址
    '''
    req = urllib.request.Request(url)   
    user_agent = ua.getRandomUA()
    req.add_header('User-Agent',user_agent)
    try:
        #模拟用户操作，每次访问至少停滞1秒
        time.sleep(1)
        response = urllib.request.urlopen(url)
        html = response.read() 
    except:
        message=traceback.format_exc()
        logger.warning('请求发送异常')
        logger.error(message)
     
    return html
                       
def  getPage(url):
    html = openTheUrl(url)
	
    if html == None :
        logger.warning('获取总页数方法失效，请检查')
        return 0
    else:
        html = html.decode('utf-8')
	#当前页面中，获得页数的起始位置
        page_comment_S = html.find('class="current-comment-page"')+30
	#当前页面中，获得页数的结束位置
        page_comment_E = html.find(']',page_comment_S)
	#截取内容
        page = html[page_comment_S:page_comment_E]
        return page
    
def getImages_List(url):
	html = openTheUrl(url).decode('utf-8')
	#存放图片地址List
	dataList = []
	#使用正则匹配
	thePattern=r'<img src="([^"]+(\.jpg|\.gif))"'
	
	dataList = re.findall(thePattern,html)
	print(dataList)
        
	return dataList
     
def saveDatas(dataUrlList):
    for index, data in enumerate(dataUrlList):
        if index % 10 == 0:
            #避免被封,每10张停15秒
            time.sleep(15)
        fileName = str(index)+'.jpg'
        index += 1
        #获取文件路径，并拼接http
        url = data[0]
        if(url.find('http:')==-1):
            url = 'http:'+url
        print(url)
        flag = False
        for i in range(1,11):
            if flag :
                break
            try :
                image = openTheUrl(url)
                flag = True
            except :
                message=traceback.format_exc()
                logger.warning('请求发送异常')
                logger.error(message)
                logger.debug('第'+str(i)+'次下载失败！正在重试')
                #访问过于频繁，暂时停止10秒
                time.sleep(10)
        with open(fileName,'wb') as f:
            if image == None:
                f.write('no data')
            else:
                f.write(image)


def download_images4G(folder='images4G'):
     #获取当前工作路径
    path = os.getcwd()

    setDir(path,folder)

    path = os.getcwd()
  
    urlHome = 'http://jandan.net/ooxx'
    #获取当前页数
    page = int(getPage(urlHome))
     
    for i in range(page):

        now_page = page - i
        pageUrl =urlHome +'/page-'+str(now_page)
        imagesUrlList = getImages_List(pageUrl)
        setDir(path,str(now_page))
        saveDatas(imagesUrlList)
          
     
if __name__  == '__main__':
    download_images4G()
