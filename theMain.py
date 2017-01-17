import urllib.request
import os
import time
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
    req = urllib.request.Request(url)
    user_agent = ua.getRandomUA()
    print(user_agent)
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
     #此处不解码，按需解码！forE：下载时就不需要解码

    return html

def  getPage(url):
    html = openTheUrl(url).decode('utf-8')
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

     #获取起始位置
     imageUrl_S = html.find('<img src="//')
     
     #对页面进行循环获取图片位置
     while imageUrl_S != -1:
          #获取结束位置
          imageUrl_E = html.find('.jpg',imageUrl_S,imageUrl_S+100)

          #如果找不到，则起始位置偏移；找得到，保存路径到List
          if imageUrl_E != -1:
               imageUrl = html[imageUrl_S+12:imageUrl_E+4]
               dataList.append(imageUrl)
          else:
               #找不到结束标记，则在原起始位置后偏移12个位置
               imageUrl_E=imageUrl_S+12

          #再次定义新的起始位置，从上次定义的结束位置处开始     
          imageUrl_S = html.find('<img src="//',imageUrl_E)
     return dataList
     
def saveDatas(dataUrlList):
     
     for index, data in enumerate(dataUrlList):
          if index % 10 == 0:
               #避免被封,每10张停15秒
               time.sleep(15)     
         
          fileName = str(index)+'.jpg'
          print(fileName)
          index += 1
          with open(fileName,'wb') as f:
               url = 'http://'+data
               image = openTheUrl(url)
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
          if(i == 10):
               break
          now_page = page - i
          pageUrl =urlHome +'/page-'+str(now_page)
          imagesUrlList = getImages_List(pageUrl)
          setDir(path,str(now_page))
          saveDatas(imagesUrlList)
          
     
if __name__  == '__main__':
    download_images4G()
