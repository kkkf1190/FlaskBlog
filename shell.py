import sys
sys.path.append('D:\\PycharmProjects\\FlaskBlog')
from model import ZhihuModel
import urllib,json,os
import urllib.request

def createFileWithFileName(localPathParam,fileName):
    totalPath=localPathParam+'\\'+fileName
    if not os.path.exists(totalPath):
        file=open(totalPath,'a+')
        file.close()
        return totalPath


localPath = 'static\\image'
url = "http://news-at.zhihu.com/api/4/news/latest"
data=urllib.request.urlopen(url).read()
z_data=data.decode('UTF-8')
items = json.loads(z_data)
stories = items['stories']
i=0
for story in stories:
    imgurl = str(stories[i]['images'][0])
    img = imgurl[22:]
    # imgdata=urllib.request.urlopen(imgurl).read()
    # print(img)
    # open(createFileWithFileName(localPath,img), "wb").write(imgdata)
    storyModel = ZhihuModel(item_id = stories[i]['id'] )
    storyModel.item_date = items['date']
    storyModel.item_title = stories[i]['title']
    storyModel.item_frontimg = str(stories[i]['images'][0])
    itemid = stories[i]['id']
    url1 = "http://news-at.zhihu.com/api/4/news/"+str(itemid)
    itemContent = urllib.request.urlopen(url1).read()
    content_data=itemContent.decode('UTF-8')
    content = json.loads(content_data)
    storyModel.item_content = content['body']
    storyModel.item_css = content['css'][0]
    storyModel.save()
    i+=1

zhihus = ZhihuModel.objects()
for zhihu in zhihus:
    url2 = str(zhihu.item_frontimg)
    frontimg = url2[22:]
    print(frontimg)
    frontimgdata=urllib.request.urlopen(url2).read()
    open(createFileWithFileName(localPath,frontimg), "wb").write(frontimgdata)
    zhihu.item_frontimg = frontimg
    zhihu.save()